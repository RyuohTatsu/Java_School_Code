"""
__filename__ = "lab3_state_data.py"
__coursename__ = "SDEV 300 7381 - Building Secure Web Applications (2208)
__author__ = "John Doe"
__copyright__ = "None"
__credits__ = ["John Doe"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Doe"
__email__ = "jdoe@student.umuc.edu"
__status__ = "Baseline"

REQUIRES MODULE INSTALL:

pip3 install Image -U
pip3 install requests -U
pip3 install matplotlib -U

"""

from PIL import Image
import requests
import matplotlib.pyplot as plt


# --------------------------------------------------------------------
# - Create State dictionary with nested dictionary (Capital and Bird)
# --------------------------------------------------------------------
# Turn off line length for this section to avoid breaking up URL
# pylint: disable=C0301
state_dict = {"Alabama": {"Capital": "Montgomery", "Bird": "Yellowhammer",
                          "Flower": "Camellia",
                          "Population": "4887870",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/camellia-flower.jpg?itok=K1xKDUI5"},
              "Alaska": {"Capital": "Juneau", "Bird": "Willow Ptarmigan",
                         "Flower": "Forget Me Not",
                         "Population": "737438",
                         "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Alpineforgetmenot.jpg?itok=VxF44TUl"},
              "Arizona": {"Capital": "Phoenix", "Bird": "Cactus Wren",
                          "Flower": "Saguaro Cactus Blossom",
                          "Population": "7171650",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/saguaroflowersFlickr.jpg?itok=DxWnZav5"},
              "Arkansas": {"Capital": "Little Rock", "Bird": "Mockingbird",
                           "Flower": "Apple Blossom",
                           "Population": "3013820",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/AppletreeblossomArkansasflower.JPG?itok=HRX6pZyN"
                           },
              "California": {"Capital": "Sacramento", "Bird": "California Valley Quail",
                            "Flower": "Golden Poppy",
                            "Population": "39557000",
                            "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CAflowerCaliforniaPoppy.jpg?itok=62onOuJf"},
              "Colorado": {"Capital": "Denver", "Bird": "Lark Bunting",
                           "Flower": "Rocky Mountain Columbine",
                           "Population": "5695560",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Colorado_columbine2.jpg?itok=3bfYnk5Y"},
              "Connecticut": {"Capital": "Hartford", "Bird": "Robin",
                              "Flower": "Mountain Laurel",
                              "Population": "3572660",
                              "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G"},
              "Delaware": {"Capital": "Dover", "Bird": "Blue Hen",
                           "Flower": "Peach Blossom",
                           "Population": "967171",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/peachblossomspeachflowers.jpg?itok=Lx-fzlgl"},
              "Florida": {"Capital": "Tallahassee", "Bird": "Mockingbird",
                          "Flower": "Orange Blossom",
                          "Population": "21299300",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/OrangeBlossomsFloridaFlower.jpg?itok=SK-Tp-rH"},
              "Georgia": {"Capital": "Atlanta", "Bird": "Brown Thrasher",
                          "Flower": "Cherokee Rose",
                          "Population": "10519500",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CherokeeRoseFlower.jpg?itok=TKWxpzcw"},
              "Hawaii": {"Capital": "Honolulu", "Bird": "Nene",
                         "Flower": "Hibiscus",
                         "Population": "1420490",
                         "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/yellowhibiscusPuaAloalo.jpg?itok=Y2aYqLKY"},
              "Idaho": {"Capital": "Boise", "Bird": "Mountain Bluebird",
                        "Flower": "Syringa",
                        "Population": "1754210",
                        "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/syringaPhiladelphuslewisiiflower.jpg?itok=BKOaOXs0"},
              "Illinois": {"Capital": "Springfield", "Bird": "Cardinal",
                           "Flower": "Violet",
                           "Population": "12741100",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/singlebluevioletflower.jpg?itok=8i1uQHwg"},
              "Indiana": {"Capital": "Indianapolis", "Bird": "Cardinal",
                          "Flower": "Peony",
                          "Population": "6691880",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/PeonyPaeoniaflowers.jpg?itok=IrFIQ9ZF"},
              "Iowa": {"Capital": "Des Moines", "Bird": "Eastern Goldfinch",
                       "Flower": "Wild Rose",
                       "Population": "3156140",
                       "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WildPrairieRose.jpg?itok=zyo0qIMG"},
              "Kansas": {"Capital": "Topeka", "Bird": "Western Meadowlark",
                         "Flower": "Sunflower",
                         "Population": "2911500",
                         "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/native-sunflowers.jpg?itok=PB8Qq-IC"},
              "Kentucky": {"Capital": "Frankfort", "Bird": "Cardinal",
                           "Flower": "Goldenrod",
                           "Population": "4468400",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/stateflowergoldenrod-bloom.jpg?itok=CCLZ4eiV"},
              "Louisiana": {"Capital": "Baton Rouge", "Bird": "Eastern Brown Pelican",
                            "Flower": "Magnolia",
                            "Population": "4659980",
                            "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MagnoliagrandifloraMagnoliaflower.jpg?itok=LQ7y9QJk"},
              "Maine": {"Capital": "Augusta", "Bird": "Chickadee",
                        "Flower": "White Pine Cone and Tassel",
                        "Population": "1338400",
                        "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/whitepinemalecones.jpg?itok=cscy757F"},
              "Maryland": {"Capital": "Annapolis", "Bird": "Baltimore Oriole",
                           "Flower": "Black-eyed Susan",
                           "Population": "6042720",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/FlowerMDBlack-eyedSusan.jpg?itok=I8jYSvFl"},
              "Massachusetts": {"Capital": "Boston", "Bird": "Chickadee",
                                "Flower": "Mayflower",
                                "Population": "6902150",
                                "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MayflowerTrailingArbutus.jpg?itok=uIQd8O6F"},
              "Michigan": {"Capital": "Lansing", "Bird": "Robin",
                           "Flower": "Apple Blossom",
                           "Population": "9995920",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/appleblossombeauty.jpg?itok=HxWn6VHl"},
              "Minnesota": {"Capital": "Saint Paul", "Bird": "Common Loon",
                            "Flower": "Lady Slipper",
                            "Population": "5611180",
                            "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/pinkwhiteladysslipperflower1.jpg?itok=LGYZFl26"},
              "Mississippi": {"Capital": "Jackson", "Bird": "Mockingbird",
                              "Flower": "Magnolia",
                              "Population": "2986530",
                              "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/magnoliablossomflower01.jpg?itok=xlIoba-H"},
              "Missouri": {"Capital": "Jefferson City", "Bird": "Bluebird",
                           "Flower": "Hawthorn",
                           "Population": "6126450",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/hawthornflowersblossoms1.jpg?itok=LOrlsJ3L"},
              "Montana": {"Capital": "Helena", "Bird": "Western Meadowlark",
                          "Flower": "Bitterroot",
                          "Population": "1062300",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/bitterrootfloweremblem.jpg?itok=SnCwy78x"},
              "Nebraska": {"Capital": "Lincoln", "Bird": "Western Meadowlark",
                           "Flower": "Goldenrod",
                           "Population": "1929270",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/goldenrodflowersyellow4.jpg?itok=6X5qpm4c"},
              "Nevada": {"Capital": "Carson City", "Bird": "Mountain Bluebird",
                         "Flower": "Sagebrush",
                         "Population": "3034390",
                         "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg?itok=ij6RMnom"},
              "New Hampshire": {"Capital": "Concord", "Bird": "Purple Finch",
                                "Flower": "Purple Lilac",
                                "Population": "1356460",
                                "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/lilacflowerspurplelilac.jpg?itok=GM5URJEO"},
              "New Jersey": {"Capital": "Trenton", "Bird": "Eastern Goldfinch",
                             "Flower": "Purple Violet",
                             "Population": "8908520",
                             "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r"},
              "New Mexico": {"Capital": "Santa Fe", "Bird": "Roadrunner",
                             "Flower": "Yucca",
                             "Population": "2095430",
                             "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/YuccaFlowersclose.jpg?itok=jCUN8toc"},
              "New York": {"Capital": "Albany", "Bird": "Bluebird",
                           "Flower": "Rose",
                           "Population": "19542200",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redrosebeautystateflowerNY.jpg?itok=LDcB_Vc_"},
              "North Carolina": {"Capital": "Raleigh", "Bird": "Cardinal",
                                 "Flower": "Dogwood",
                                 "Population": "10383600",
                                 "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg?itok=p_1PGcNk"},
              "Ohio": {"Capital": "Columbus", "Bird": "Cardinal",
                       "Flower": "Scarlet Carnation",
                       "Population": "11689400",
                       "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WhitetrilliumTrilliumgrandiflorum.jpg?itok=oGiuGS6p"},
              "Oklahoma": {"Capital": "Oklahoma City", "Bird": "Scissor-Tailed Flycatcher",
                           "Flower": "Mistletoe",
                           "Population": "3943080",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/mistletoe_phoradendron_serotinum.jpg?itok=7W9kY8YB"},
              "Oregon": {"Capital": "Salem", "Bird": "Western Meadowlark",
                         "Flower": "Oregon Grape",
                         "Population": "4190710",
                         "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Oregongrapeflowers2.jpg?itok=lVSJoqCE"},
              "Pennsylvania": {"Capital": "Harrisburg", "Bird": "Ruffed Grouse",
                               "Flower": "Mountain Laurel",
                               "Population": "12807100",
                               "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Mt_Laurel_Kalmia_Latifolia.jpg?itok=8VhW2Sms"},
              "Rhode Island": {"Capital": "Providence", "Bird": "Rhode Island Red",
                               "Flower": "Violet",
                               "Population": "1057320",
                               "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/violetsflowers.jpg?itok=KNMrrLfu"},
              "South Carolina": {"Capital": "Columbia", "Bird": "Great Carolina Wren",
                                 "Flower": "Carolina Yellow Jessamine",
                                 "Population": "5084130",
                                 "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CarolinaYellowJessamine101.jpg?itok=1tgcX6mj"},
              "North Dakota": {"Capital": "Bismarck", "Bird": "Western Meadowlark",
                               "Flower": "Wild Prairie Rose",
                               "Population": "760077",
                               "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flowerwildprairierose.jpg?itok=j5Retaxz"},
              "South Dakota": {"Capital": "Pierre", "Bird": "Ring-Necked Pheasant",
                               "Flower": "American Pasqueflower",
                               "Population": "882235",
                               "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Pasqueflower-03.jpg?itok=vMlGt_qW"},
              "Tennessee": {"Capital": "Nashville", "Bird": "Mockingbird",
                            "Flower": "Iris",
                            "Population": "6770010",
                            "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/purpleirisflower.jpg?itok=ZJjHu7Lb"},
              "Texas": {"Capital": "Austin", "Bird": "Mockingbird",
                        "Flower": "Bluebonnet",
                        "Population": "28701800",
                        "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/EnnisTXbluebonnetfield.jpg?itok=H8r2UOSJ"},
              "Utah": {"Capital": "Salt Lake City", "Bird": "California Seagull",
                       "Flower": "Sego Lily",
                       "Population": "3161100",
                       "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/SegoLily.jpg?itok=Hxt3DOTq"},
              "Vermont": {"Capital": "Montpelier", "Bird": "Hermit Thrush",
                          "Flower": "Red Clover",
                          "Population": "626299",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcloverstateflowerWV.jpg?itok=wvnkPA4C"},
              "Virginia": {"Capital": "Richmond", "Bird": "Cardinal",
                           "Flower": "American Dogwood",
                           "Population": "8517680",
                           "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringDogwoodSpring.jpg?itok=DFuNFYgS"},
              "Washington": {"Capital": "Olympia", "Bird": "Willow Goldfinch",
                             "Flower": "Coast Rhododendron",
                             "Population": "7535590",
                             "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flower_rhododendronWeb.jpg?itok=0Xl911Zf"},
              "West Virginia": {"Capital": "Charleston", "Bird": "Cardinal",
                                "Flower": "Rhododendron",
                                "Population": "1805830",
                                "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/rhododendronWVstateflower.jpg?itok=7lJaeqWT"},
              "Wisconsin": {"Capital": "Madison", "Bird": "Robin",
                            "Flower": "Wood Violet",
                            "Population": "5813570",
                            "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r"},
              "Wyoming": {"Capital": "Cheyenne", "Bird": "Western Meadowlark",
                          "Flower": "Indian Paintbrush",
                          "Population": "577737",
                          "URL": "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/indianpaintbrushWYflower.jpg?itok=ClQHPA55"}
              }
# Turn on line length for rest of code
# pylint: enable=C0301

def display_state_flower(state_dict_local, state):
    """ Searches for the given state to display the flower """

    if state in state_dict_local:
        url_pic = state_dict_local[state]["URL"]
        response = requests.get(url_pic, stream=True)
        img = Image.open(response.raw)
        img.show()
    else:
        print("\nState '{}' does not exist.".format(state))

def display_sorted_states(state_dict_local):
    """ Displays states, capitals and Birds sorted by state (Key)"""

    state_sorted_dict = dict(sorted(state_dict_local.items()))

    for state_name in state_sorted_dict.keys():
        print("State Name:", state_name,
              "\n\t    Capital:", state_sorted_dict[state_name]["Capital"],
              "\n\t    Flower:", state_sorted_dict[state_name]["Flower"],
 #             "\n\t    Bird:", state_sorted_dict[state_name]["Bird"],
              "\n\t    Population:",
              state_sorted_dict[state_name]["Population"])


def get_state_info_and_bird(state_dict_local, state):
    """ Searches for the given state to display the states info and bird """

    if state in state_dict_local:
        print("\nState found: ", state)
        print("Capital:", state_dict_local[state]["Capital"])
        print("Flower:", state_dict_local[state]["Flower"])
#        print("Bird:", state_dict_local[state]["Bird"])
        print("Population:", state_dict_local[state]["Population"])

        display_state_flower(state_dict_local, state)

    else:
        print("\nState '{}' does not exist.".format(state))


def update_state_population(state_dict_local, state, population):
    """ Method will locate the given state and update the state population """
    if state in state_dict:
        # ----------------------------------
        # - Update state population with new info
        # ----------------------------------
        print("\nOld State Population:",
              state_dict_local[state]["Population"])
        state_dict_local[state]["Population"] = population
        print("New State Population:", state_dict_local[state]["Population"])
        print("** {}'s state population has been changed to {}"\
              .format(state, population))
    else:
        print(
            "\nUnable to update {}'s state population because state does not"\
            "exist.".format(state)
             )

def main():
    """
    Lab3 main()
    """

    # ------------------
    # - Welcome message
    # ------------------
    print("-" * 57)
    print("*** Welcome to the State Capital and Bird application ***")
    print("-" * 57)

    # -----------------------
    # - Display menu to user
    # -----------------------
    user_input = 0

    while user_input != 5:
        print("1. Display all U.S. States in Alphabetical order along with "\
              "the Capital, State Population, and Flower")
        print("2. Search for a specific state and display the appropriate "\
              "Capital name, State Population, and an image of the "\
              "associated State Flower.")
        print("3. Provide a Bar graph of the top 5 populated States "\
              "showing their overall population.")
        print("4. Update the overall state population for a specific state.")
        print("5. Exit the program")

        user_input = int(input("\nEnter Selection: "))

        # ----------------------------
        # - Check for user selection
        # ----------------------------
        if user_input == 1:
            display_sorted_states(state_dict)

        elif user_input == 2:
            # - Make sure you title case input
            state_name_input = input(
                "\nEnter state name to search for: ").title()
            get_state_info_and_bird(state_dict, state_name_input)

        elif user_input == 3:
            top_state = []
            state_population = []
            states_data = []
            # Map to a simpler Array for Lambda function
            for state in state_dict:
                states_data.append({"State": state,
                                    "Population":
                                    int(state_dict[state]["Population"])})
            # Sort based on Population descending
            all_states_pop = sorted(
                states_data, key=lambda i: i["Population"], reverse=True)

            # Build the Bar Graph
            print("\r\n","Top 5 State populations for Graphic:")
            for top_5 in all_states_pop[:5]:
                print("\t",top_5["State"],top_5["Population"])
                top_state.append(top_5["State"])
                state_population.append(top_5["Population"])
            print("\r\n")
            plt.ylabel('State Population')
            plt.xlabel('States')
            plt.ticklabel_format(style='plain')
            plt.bar(top_state, state_population, width=0.5,
                    color='#008fd5', edgecolor='black')
            plt.text(0, 0, 'POSTED BY PROFESSOR POMA',
                     horizontalalignment='center',
                     color='gray', alpha=0.5, verticalalignment='center')
            plt.show()
            plt.clf()
            plt.close()

        elif user_input == 4:
            state, population = input("\nEnter the name of the State and"
                                "new population.\n"
                                "Seperate the State from the new "
                                "population with a comma (example:"
                                " Maryland, 200000): ").split(",")
            update_state_population(
                state_dict, state.strip().title(), population.strip().title())

    print("** Thank you for using the State Capital and Bird application **")


if __name__ == "__main__":
    main()
