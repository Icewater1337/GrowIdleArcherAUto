import image_clicker_tool as clicker
import time

# Needs fullscreen on top screen (1920x 1080 res)

def login_to_account(login_type,username = None, pw = None):
    logout()
    if login_type == 'facebook' and username is not None and pw is not None:
        clicker.executeClickASAP("imagess/facebook_login.png")
        clicker.executeClickASAP("imagess/fb_username.png")
        clicker.type(username)
        clicker.executeClickASAP("imagess/fb_pw.png")
        clicker.type(pw)
        clicker.executeClickASAP("imagess/fb_login.png")
        clicker.executeClickASAP("imagess/fb_next.png")

    if login_type == 'google':
        clicker.executeClickASAP("imagess/google_play_login.png")
        clicker.executeClickASAP("imagess/gp_cancel_1.png")
        clicker.executeClickASAP("imagess/gp_2.png")
        clicker.executeClickASAP("imagess/gp_3.png")
        clicker.executeClickASAP("imagess/gp_4.png")

    clicker.executeClickASAP("imagess/ulala_start.png")
    return


def logout_character():
    clicker.executeClickASAP("imagess/ulala_settings.png")
    clicker.executeClickASAP("imagess/ulala_switch_character.png")




def login_to_character(character_class):
    img = "imagess/{}.png".format(character_class)

    pos = 0
    while not clicker.is_images_found(img):
        print("char not found yet")
        clicker.click_character_pos(pos)
        pos += 1


    clicker.executeClickASAP("imagess/ulala_start.png")

    return


def expeditions():
    clicker.executeClickASAP("imagess/ulala_pet.png")
    clicker.executeClickASAP("imagess/ulala_explore.png")
    clicker.executeClickASAP("imagess/ulala_explore_2.png")
    clicker.executeClickASAP("imagess/ulala_adventure_claim.png")
    clicker.executeClickASAP("imagess/ulala_adventure_tap_continue.png")
    clicker.executeClickASAP("imagess/ulala_adventure_quick.png")
    clicker.executeClickASAP("imagess/ulala_adventure_quick_join.png")
    clicker.executeClickASAP("imagess/ulala_adventure_quick_start.png")
    clicker.executeClickASAP("imagess/ulala_adventure_back.png")
    clicker.executeClickASAP("imagess/ulala_home.png")

def capture_pet():
    clicker.executeClickASAP("imagess/ulala_pet.png")
    clicker.executeClickASAP("imagess/ulala_capture_still.png")
    time.sleep(2)
    pos =  clicker.returnPosIfExists("imagess/ulala_capture_btn.png")
    if pos is not None:
        clicker.executeClickASAP("imagess/ulala_capture_btn.png")
        clicker.executeClickASAP("imagess/ulala_tap_continue.png")
        time.sleep(4)
        while clicker.returnPosIfExists("imagess/ulala_add_food.png") is None:
            clicker.executeClickASAP("imagess/ulala_tap_continue.png")
            time.sleep(4)

    clicker.executeClickASAP("imagess/ulala_add_food.png")
    time.sleep(2)
    if not (clicker.executeClickIfExists("imagess/ulala_green_good.png")):
        if not ( clicker.executeClickIfExists("imagess/ulala_blue_food.png")):
            clicker.executeClickIfExists("imagess/ulala_purple_food.png")
    time.sleep(1)
    clicker.executeClickIfExists("imagess/ulala_confirm.png")

    clicker.executeClickASAP("imagess/ulala_back_pet.png")

    clicker.executeClickASAP("imagess/ulala_home.png")



def smelt_gear():
    clicker.executeClickASAP("imagess/ulala_storage.png")
    clicker.executeClickASAP("imagess/ulala_storage_smelt.png")
    clicker.executeClickASAP("imagess/ulala_storage_smelt.png")
    clicker.executeClickASAP("imagess/ulala_storage_tap_continue.png")
    clicker.executeClickASAP("imagess/ulala_storage_back.png")


def fuse_gems():
    clicker.executeClickASAP("imagess/ulala_storage.png")
    clicker.executeClickASAP("imagess/ulala_storage_gem.png")
    clicker.executeClickASAP("imagess/ulala_storage_quick_fuse.png")
    clicker.executeClickASAP("imagess/ulala_storage_quick_fuse_confirm.png")
    clicker.executeClickASAP("imagess/ulala_storage_tap_continue.png")
    clicker.executeClickASAP("imagess/ulala_storage_back.png")


def release_pet():
    clicker.executeClickASAP("imagess/ulala_pet.png")
    clicker.executeClickASAP("imagess/ulala_pet_release.png")
    time.sleep(2)
    clicker.executeClickASAP("imagess/ulala_pet_by_quality.png")
    time.sleep(2)
    clicker.executeClickASAP("imagess/ulala_pet_normal.png")
    time.sleep(1)
    clicker.executeClickASAP("imagess/ulala_pet_uncommon.png")
    time.sleep(1)
    clicker.executeClickASAP("imagess/ulala_pet_confirm.png")
    time.sleep(1)
    clicker.executeClickASAP("imagess/ulala_pet_confirm.png")
    time.sleep(1)
    clicker.executeClickASAP("imagess/ulala_home.png")

def quick_boost():
    clicker.executeClickASAP("imagess/ulala_fight.png")
    clicker.executeClickASAP("imagess/quick_battle.png")
    clicker.executeClickASAP("imagess/free_boost.png")
    clicker.executeClickASAP("imagess/ulala_home.png")

def cook():
    clicker.executeClickASAP("imagess/ulala_cook.png")
    clicker.executeClickASAP("imagess/ulala_food_recipes.png")
    clicker.click_pos(1422, 1122)
    clicker.executeClickASAP("images/ulala_food_cook.png")
    clicker.executeClickASAP("images/ulala_food_cooking.png")
    clicker.executeClickASAP("images/ulala_food_tap_storage.png")
    clicker.executeClickASAP("images/ulala_food_back.png")




def collect_dailies():
    clicker.executeClickASAP("images/ulala_quests.png")
    clicker.executeClickASAP("images/ulala_quests_dailies.png")
    clicker.executeClickASAP("images/ulala_quests_accept.png")
    clicker.executeClickASAP("images/ulala_daily_1.png")



def quick_enhance():
    pass

def crystal_fuse():
    pass

def skill_consume():
    clicker.executeClickASAP("images/ulala_team.png")
    clicker.executeClickASAP("images/ulala_skill.png")
    clicker.executeClickASAP("images/ulala_skill_storage.png")
    clicker.executeClickASAP("images/ulala_skill_storage_close.png")
    clicker.executeClickASAP("images/ulala_skill_back.png")
    clicker.executeClickASAP("images/ulala_home.png")


def logout():
    clicker.executeClickIfExists("imagess/logout.png")


def skip_start_screen():
    img = "imagess/ulala_accept.png"
    close_img = "imagess/ulala_close.png"

    time.sleep(20)
    clicker.executeClickIfExists(img)
    time.sleep(5)
    clicker.executeClickIfExists(img)
    time.sleep(3)
    clicker.executeClickIfExists(close_img)
    time.sleep(3)
    clicker.executeClickIfExists(close_img)


def enchant_archery():
    print("click on archery")
    clicker.executeClickASAP("images/enchant_archery.png")
    time.sleep(1)
    print("click on archery inside archery")
    clicker.click_pos(1200,275)
    time.sleep(1)
    print("scroll to top")
    clicker.click_pos(1400, 509)
    time.sleep(1)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    print("scroll up done")
    time.sleep(1)


    print("enchant first three")
    # first enchant
    print("start clicking on learn")
    while clicker.is_image_found("images/learn.png"):
        time.sleep(0.5)
        clicker.executeClickIfExists("images/learn.png")

    print("clicking learn done")
    print("start clicking on upgrades")

    clicker.click_pos(2236, 605)
    time.sleep(0.5)

    clicker.click_pos(2229, 968)
    time.sleep(0.5)

    print("upgrade done")
    time.sleep(0.5)
    print("scroll down")
    clicker.click_pos(1400, 509)
    time.sleep(1)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)

    print("start clicking on learn")
    while clicker.is_image_found("images/learn.png"):
        time.sleep(0.5)
        clicker.executeClickIfExists("images/learn.png")

    print("clicking learn done")
    print("start clicking on upgrades")

    clicker.click_pos(2236, 445)
    time.sleep(0.5)

    clicker.click_pos(2229, 793)
    time.sleep(0.5)

    clicker.click_pos(2229, 1088)
    time.sleep(0.5)

    print("upgrade done")

    time.sleep(1)
    print("go back")
    clicker.executeClickASAP("images/cross_close.png")
    time.sleep(1)
    print("enchant archery rota done")


def click_level_up_or_create(loop_nbr):
    print("start clicking levelup/create")
    for i in range(0,loop_nbr):
        clicker.executeClickIfExists("images/create.png")
        time.sleep(0.5)
        clicker.executeClickIfExists("images/levelup.png")
        time.sleep(0.5)




def enchant_steel(loop_nbr):
    clicker.click_pos(2389, 483)
    click_level_up_or_create(loop_nbr)

def enchant_bomb(loop_nbr):
    clicker.click_pos(2432, 740)
    click_level_up_or_create(loop_nbr)


def enchant_energy(loop_nbr):
    clicker.click_pos(2389, 975)
    click_level_up_or_create(loop_nbr)


def enchant_poison(loop_nbr):
    clicker.click_pos(2389, 1183)
    click_level_up_or_create(loop_nbr)


def enchant_ice(loop_nbr):
    clicker.click_pos(2389, 708)
    click_level_up_or_create(loop_nbr)


def enchant_big(loop_nbr):
    clicker.click_pos(2389, 905)
    click_level_up_or_create(loop_nbr)


def enchant_light(loop_nbr):
    clicker.click_pos(2389, 1163)
    click_level_up_or_create(loop_nbr)


def enchant_seed(loop_nbr):
    clicker.click_pos(2389, 460)
    click_level_up_or_create(loop_nbr)


def enchant_sharp(loop_nbr):
    clicker.click_pos(2389, 683)
    click_level_up_or_create(loop_nbr)


def enchant_lightning(loop_nbr):
    clicker.click_pos(2389, 980)
    click_level_up_or_create(loop_nbr)


def enchant_lava(loop_nbr):
    clicker.click_pos(2389, 1133)
    click_level_up_or_create(loop_nbr)


def enchant_arrows(loop_nbr_dict):

    clicker.executeClickASAP("images/enchants_1.png")
    time.sleep(1)
    print("clicking on levelup")
    clicker.click_pos(918, 257)
    time.sleep(1)
    scroll_up_all()
    time.sleep(1)
    print("start to enchant steel")
    enchant_steel(loop_nbr_dict["steel"])
    print("start to enchant bomb")
    enchant_bomb(loop_nbr_dict["bomb"])
    print("start to enchant energy")
    enchant_energy(loop_nbr_dict["energy"])
    print("start to enchant poison")
    enchant_poison(loop_nbr_dict["poison"])
    scroll_down_enchantment_research_first()
    print("start to enchant ice")
    enchant_ice(loop_nbr_dict["ice"])
    print("start to enchant big")
    enchant_big(loop_nbr_dict["big"])
    print("start to enchant light")
    enchant_light(loop_nbr_dict["light"])
    scroll_down_enchant_reserach_second()
    print("start to enchant seed")
    enchant_seed(loop_nbr_dict["seed"])
    print("start to enchant sharp")
    enchant_sharp(loop_nbr_dict["sharp"])
    print("start to enchant lioghtning")
    enchant_lightning(loop_nbr_dict["lightning"])
    print("start to enchant lava")
    enchant_lava(loop_nbr_dict["lava"])

    clicker.executeClickASAP("images/cross_close.png")
    time.sleep(1)
    print("enchanting done")


def scroll_down_enchant_reserach_second():
    print("attempt to scroll down")
    clicker.click_pos(2389, 980)
    time.sleep(1)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    print("scroll down enchantment/reserach done")


def scroll_down_enchantment_research_first():
    print("start scrolling down")
    # click last locationagain to scroll from there
    clicker.click_pos(2389, 1183)
    clicker.scroll_down(100)
    time.sleep(0.5)
    clicker.scroll_down(100)
    time.sleep(0.5)
    print("scrolling down enchantments/reserach done")


def scroll_up_all():
    print("attempt to scroll up")
    clicker.click_pos(2400, 511)
    time.sleep(1)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    time.sleep(0.5)
    clicker.scroll_up(100)
    print("scroll up done")



def start_autoclicker():
    time.sleep(1)
    clicker.executeClickASAP("images/start_ac.png")



def stop_auto_clicker():
    time.sleep(1)
    clicker.executeClickASAP("images/stop_ac.png")


def reincarnate():
    print("click reincarnate")
    clicker.executeClickASAP("images/reincarnate.png")
    print("click reincarnate in reincarnate")
    clicker.executeClickASAP("images/reincarnate_reincarnate.png")
    print("click yes")
    clicker.executeClickASAP("images/yes.png")
    time.sleep(5)
    print("reincarnation done")


def quick_firing():
    print("activate quick firing")
    clicker.click_pos(1400,630)
    clicker.executeClickASAP("images/buffs_activate.png")
    print("done activating quickfire")
    time.sleep(1)


def critical_strike():
    print("activate crit")
    clicker.click_pos(2500, 630)
    clicker.executeClickASAP("images/buffs_activate.png")
    print("done crit")
    time.sleep(1)


def stealing_gold():
    print("activate quick firing")
    clicker.click_pos(2500, 1000)
    clicker.executeClickASAP("images/buffs_activate.png")
    print("done activating quickfire")
    time.sleep(1)


def use_buffs():
    print("using buffs")
    clicker.executeClickASAP("images/buffs.png")
    time.sleep(1)
    print("click on buff")
    clicker.click_pos(1300,276)
    time.sleep(1)
    quick_firing()
    critical_strike()
    stealing_gold()
    clicker.executeClickIfExists("images/cross_close.png")
    time.sleep(1)
    clicker.executeClickIfExists("images/cross_close.png")
    time.sleep(1)


def research_elt():
    time.sleep(1)
    for i in range(0, 3):
        if clicker.is_image_found("images/enchants_available_enchant_click.png"):
            clicker.executeClickASAP("images/enchants_available_enchant_click.png")
            time.sleep(2)
        else:
            print("scroll down a bit")
            clicker.click_pos(1237, 816)
            time.sleep(0.5)
            clicker.scroll_down(100)
            time.sleep(0.5)



def research_steel():
    clicker.click_pos(2389, 483)
    research_elt()

def research_bomb():
    clicker.click_pos(2432, 740)
    research_elt()


def research_energy():
    clicker.click_pos(2389, 975)
    research_elt()


def research_poison():
    clicker.click_pos(2389, 1183)
    research_elt()


def research_ice():
    clicker.click_pos(2389, 708)
    research_elt()


def research_big():
    clicker.click_pos(2389, 905)
    research_elt()


def research_light():
    clicker.click_pos(2389, 1163)
    research_elt()


def research_seed():
    clicker.click_pos(2389, 460)
    research_elt()


def research_sharp():
    clicker.click_pos(2389, 683)
    research_elt()


def research_lightning():
    clicker.click_pos(2389, 980)
    research_elt()


def research_lava():
    clicker.click_pos(2389, 1133)
    research_elt()


def start_arrow_research_if_possible():
    # comment in when needed
    print("attempting to start arrow research")
    print("open enchants")
    clicker.executeClickASAP("images/enchants_1.png")
    time.sleep(1)
    print("click on research")
    clicker.click_pos(1300,275)
    time.sleep(1)
    scroll_up_all()
    time.sleep(1)
    print("start to research steel")
    research_steel()
    print("start to research bomb")
    research_bomb()
    print("start to research energy")
    research_energy()
    # print("start to research poison")
    # research_poison()
    # scroll_down_enchantment_research_first()
    # print("start to research ice")
    # research_ice()
    # print("start to research big")
    # research_big()
    # print("start to research light")
    # research_light()
    # scroll_down_enchant_reserach_second()
    # print("start to research seed")
    # research_seed()
    # print("start to research sharp")
    # research_sharp()
    # print("start to research lioghtning")
    # research_lightning()
    # print("start to research lava")
    # research_lava()
    # print("researching done")
    clicker.executeClickASAP("images/cross_close.png")
    time.sleep(5)


def release_town_rotation():
    print("start town rotation")
    print("open town")
    clicker.executeClickASAP("images/town.png")
    time.sleep(1)
    print("click on town reincarnation")
    clicker.click_pos(2136,343)
    time.sleep(1)
    print("click reincarnate all residents")
    clicker.executeClickASAP("images/town_rein_resi.png")
    print("click yes")
    clicker.executeClickASAP("images/yes.png")
    time.sleep(10)
    print("open town")
    clicker.executeClickASAP("images/town.png")
    time.sleep(1)
    print("click town defense")
    clicker.click_pos(1688,343)
    time.sleep(1)
    print("activate auto progress if not already")
    clicker.executeClickIfExists("images/auto_rogress_empty.png")
    time.sleep(1)
    print("start battle")
    clicker.executeClickASAP("images/town_start_battle.png")
    print("start autoclicker rota for 10 min")
    autoclicker_rotation(1200)




def execute_routine():
    start_time = time.time()
    reset_counter = 0
    enchant_counter = 0
    time.sleep(5)

    if reset_counter == 3:
        release_town_rotation()
        reset_counter = 0

    while(True):
        reincarnate()
        reset_counter += 1

        enchant_archery()
        time.sleep(10)

        loop_nbr_dict_1 = {"steel": 9, "bomb": 3, "energy": 3, "poison": 3, "ice": 1, "big": 1, "light": 1, "seed": 1,
                         "sharp": 1, "lightning": 0, "lava": 0 }
        enchant_arrows(loop_nbr_dict_1)
        start_arrow_research_if_possible()
        autoclicker_rotation()
        start_arrow_research_if_possible()
        loop_nbr_dict_2 = {"steel": 5, "bomb": 4, "energy": 4, "poison": 4, "ice": 4, "big": 2, "light": 1, "seed": 1,
                         "sharp": 0, "lightning": 0, "lava": 0, }
        enchant_arrows(loop_nbr_dict_2)
        autoclicker_rotation()
        start_arrow_research_if_possible()
        loop_nbr_dict_3 = {"steel": 2, "bomb": 3, "energy": 2, "poison": 1, "ice": 1, "big": 1, "light": 1, "seed": 1,
                         "sharp": 1, "lightning": 1, "lava": 1, }
        enchant_arrows(loop_nbr_dict_3)
        time.sleep(1)
        use_buffs()
        autoclicker_rotation()


def autoclicker_rotation(time_to_execute = 300):
    print("start autoclicker")
    start_autoclicker()
    time.sleep(time_to_execute)
    stop_auto_clicker()
    print("autoclicekr ended")




execute_routine()

# execute_routine("facebook", username=username, pw=pw)

# execute_routine("google",["hunter"])