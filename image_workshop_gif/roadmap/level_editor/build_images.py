import os
import numpy as np
import cv2


MAP_COORD = 238, 140

GAME_ELEM_X = 292
GAME_ELEM_Y = 98
GAME_ELEM_W = 32
GAME_ELEM_H = 32
CURSOR_THICKNESS = 5
CURSOR_COLOR = (0, 50, 255)
VALID_CHECKBOX_COORD = 808, 4

GAME_ELEMS = (
    "nothing", "wall", "cold", "hot", "sponge",
    "tunnel_v", "tunnel_h", "elec_v", "elec_h",
    "pool", "h2o_in", "h2o_out",
)
GAME_ELEMS = dict(zip(GAME_ELEMS, range(len(GAME_ELEMS))))

ANIM_STEPS = (
    ("map", 0),
    ("cursor", "wall"),
    ("map", 67),
    ("cursor", "elec_v"),
    ("map", 70),
    ("cursor", "elec_h"),
    ("map", 72),
    ("cursor", "elec_v"),
    ("map", 74),
    ("cursor", "elec_h"),
    ("map", 77),
    ("cursor", "hot"),
    ("map", 79),
    ("cursor", "h2o_in"),
    ("map", 80),
    ("cursor", "cold"),
    ("map", 82),
    ("cursor", "hot"),
    ("map", 83),
    ("cursor", "tunnel_v"),
    ("map", 85),
    ("cursor", "pool"),
    ("map", 86),
    ("cursor", "tunnel_h"),
    ("map", 89),
    ("cursor", "tunnel_v"),
    ("map", 91),
    ("cursor", "elec_v"),
    ("map", 94),
    ("cursor", "elec_h"),
    ("map", 96),
    ("cursor", "pool"),
    ("map", 97),
    ("cursor", "cold"),
    ("map", 98),
    ("cursor", "h2o_out"),
    ("valid", True),
    ("map", 99),
    ("cursor", "hot"),
    ("map", 100),
    ("cursor", "sponge"),
    ("map", 101),
    ("cursor", "elec_h"),
    ("map", 102),




)


def blit_img(source_img, dest_img, dest_upleft_xy):
    dest_upleft_x, dest_upleft_y = dest_upleft_xy
    size_y, size_x = source_img.shape[:2]

    dest_img[
        dest_upleft_y : dest_upleft_y + size_y,
        dest_upleft_x : dest_upleft_x + size_x,
    ] = source_img


def show_cursor(dest_img, game_elem_name):

    selected_game_elem_x = GAME_ELEM_X + GAME_ELEMS[game_elem_name] * 42

    horiz_bar_start_x = selected_game_elem_x - CURSOR_THICKNESS
    horiz_bar_end_x = horiz_bar_start_x + GAME_ELEM_W + 2 * CURSOR_THICKNESS
    dest_img[
        GAME_ELEM_Y - CURSOR_THICKNESS:GAME_ELEM_Y,
        horiz_bar_start_x:horiz_bar_end_x
    ] = CURSOR_COLOR
    dest_img[
        GAME_ELEM_Y + GAME_ELEM_H:GAME_ELEM_Y + GAME_ELEM_H + CURSOR_THICKNESS,
        horiz_bar_start_x:horiz_bar_end_x
    ] = CURSOR_COLOR

    vertic_bar_start_y = GAME_ELEM_Y - CURSOR_THICKNESS
    vertic_bar_end_y = vertic_bar_start_y + GAME_ELEM_H + 2 * CURSOR_THICKNESS
    dest_img[
        vertic_bar_start_y:vertic_bar_end_y,
        horiz_bar_start_x:horiz_bar_start_x + CURSOR_THICKNESS,
    ] = CURSOR_COLOR
    dest_img[
        vertic_bar_start_y:vertic_bar_end_y,
        horiz_bar_end_x - CURSOR_THICKNESS:horiz_bar_end_x,
    ] = CURSOR_COLOR


def create_one_image(
    main_frame, level_img_index, game_elem_name,
    out_img_index, img_valid
):
    processed_image = np.array(main_frame)
    level_image_filename = f"canvas{level_img_index:03}.png"
    level_image = cv2.imread(level_image_filename)
    blit_img(level_image, processed_image, MAP_COORD)
    blit_img(img_valid, processed_image, VALID_CHECKBOX_COORD)
    show_cursor(processed_image, game_elem_name)

    out_image_path_file = f"temp_img/processed_{out_img_index:03}.png"
    # print(f"Je génère l'image numéro {out_img_index}, à partir de la source {level_img_index}")
    cv2.imwrite(out_image_path_file, processed_image)
    return processed_image


def main():
    main_frame = cv2.imread("main_frame.png")
    img_valid_false = cv2.imread("valid_false.png")
    img_valid_true = cv2.imread("valid_true.png")

    level_img_index = -1
    out_img_index = -1
    game_elem_name = "nothing"
    current_img_valid = img_valid_false

    folder = "temp_img"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.unlink(file_path)

    for step_type, step_detail in ANIM_STEPS:

        if step_type == "cursor":
            game_elem_name = step_detail
            out_img_index += 1
            create_one_image(
                main_frame, level_img_index, game_elem_name,
                out_img_index, current_img_valid,
            )
        elif step_type == "map":
            final_level_img_index = step_detail
            while level_img_index < final_level_img_index:
                level_img_index += 1
                out_img_index += 1
                create_one_image(
                    main_frame, level_img_index, game_elem_name,
                    out_img_index, current_img_valid,
                )
        if step_type == "valid":
            valid_val = step_detail
            current_img_valid = img_valid_true if valid_val else img_valid_false

    # cv2.imshow("Image", processed_image)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
