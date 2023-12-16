# --- Day 5: If You Give A Seed A Fertilizer ---

# You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

# "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

# "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

# "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

# You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

# The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

# For example:

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

# The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

# The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

# Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

# Consider again the example seed-to-soil map:

# 50 98 2
# 52 50 48

# The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

# The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

# So, the entire list of seed numbers and their corresponding soil numbers looks like this:

# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

# With this map, you can look up the soil number required for each initial seed number:

#     Seed number 79 corresponds to soil number 81.
#     Seed number 14 corresponds to soil number 14.
#     Seed number 55 corresponds to soil number 57.
#     Seed number 13 corresponds to soil number 13.

# The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

#     Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#     Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#     Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#     Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# So, the lowest location number in this example is 35.

# What is the lowest location number that corresponds to any of the initial seed numbers?

def map(input, maps):
    map_list = [i for i in range(input*10)]

    for i, map in enumerate(maps):
        source, destination, map_range = map
        replace_range = []

        for num in range(map_range):
            replace_range.append(source+num)
            map_list.remove(source+num)

        map_list = map_list[:destination] + \
            replace_range + map_list[destination:]

    output = map_list[input]

    return output


def recurrsion(input, layer=0, prev=0):
    maps = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    ]

    result = None

    if (layer < len(maps)):
        print(input)
        result = map(input, maps[layer])
        return recurrsion(result, layer+1, prev=input)
    else:
        print(input)
        return input


t_seeds = [79, 14, 55, 13]

t_seed_to_soil = [
    [50, 98, 2],
    [52, 50, 48]
]

t_soil_to_fertilizer = [
    [0, 15, 37],
    [37, 52, 2],
    [39, 0, 15]
]

t_fertilizer_to_water = [
    [49, 53, 8],
    [0, 11, 42],
    [42, 0, 7],
    [57, 7, 4]
]

t_water_to_light = [
    [88, 18, 7],
    [18, 25, 70]
]

t_light_to_temperature = [
    [45, 77, 23],
    [81, 45, 19],
    [68, 64, 13]
]

t_temperature_to_humidity = [
    [0, 69, 1],
    [1, 0, 69]
]

t_humidity_to_location = [
    [60, 56, 37],
    [56, 93, 4]
]

seeds = [
    3127166940,
    109160474,
    3265086325,
    86449584,
    1581539098,
    205205726,
    3646327835,
    184743451,
    2671979893,
    17148151,
    305618297,
    40401857,
    2462071712,
    203075200,
    358806266,
    131147346,
    1802185716,
    538526744,
    635790399,
    705979250
]

seed_to_soil = [
    [931304316, 1786548802, 232453384],
    [3500539319, 2322065235, 6421609],
    [496396007, 147739714, 266329192],
    [3169724489, 768672891, 39526579],
    [3689153715, 1361862036, 346985],
    [1936948751, 3328259881, 542896984],
    [3209251068, 3154345676, 173914205],
    [1163757700, 2814318523, 24125066],
    [2484210664, 1362209021, 231487475],
    [3991904247, 2133571422, 188493813],
    [1187882766, 4045525873, 83717994],
    [861951350, 3084992710, 69352966],
    [2715698139, 2838443589, 43714032],
    [3830303258, 4025104215, 20421658],
    [768672891, 1268583577, 93278459],
    [4180398060, 2019002186, 114569236],
    [3689500700, 1593696496, 10659519],
    [1271600760, 808199470, 460384107],
    [166497091, 526585653, 102729094],
    [3700160219, 3894961176, 130143039],
    [2966889400, 2882157621, 202835089],
    [147739714, 414068906, 18757377],
    [3850724916, 4133608796, 141179331],
    [2759412171, 2328486844, 183672918],
    [2479845735, 4129243867, 4364929],
    [3480360150, 4274788127, 20179169],
    [402636637, 432826283, 93759370],
    [3383165273, 2717123646, 97194877],
    [3506960928, 1604356015, 182192787],
    [269226185, 629314747, 133410452],
    [2943085089, 3871156865, 23804311],
    [1731984867, 2512159762, 204963884]
]

soil_to_fertilizer = [
    [3368312743, 826425240, 243745914],
    [1045038113, 3682756471, 174490549],
    [3931158487, 1530223690, 363808809],
    [1219528662, 2460222182, 131099318],
    [3020480207, 1894032499, 63879875],
    [121779694, 248970341, 36319877],
    [1993634034, 2662348686, 86667553],
    [3612058657, 1323325837, 196530127],
    [1531175223, 2604354699, 57993987],
    [158099571, 121779694, 127190647],
    [1867147432, 3317666386, 126486602],
    [2080301587, 2768963716, 548702670],
    [1402482267, 1070171154, 21180243],
    [2959841028, 4051272297, 60639179],
    [834756529, 1966243663, 128160296],
    [3911211010, 2749016239, 19947477],
    [962916825, 3857247020, 82121288],
    [2629004257, 3444152988, 238603483],
    [826425240, 1957912374, 8331289],
    [1350627980, 3939368308, 51854287],
    [1589169210, 4214533702, 80433594],
    [2867607740, 2094403959, 92233288],
    [1669602804, 1125781209, 197544628],
    [3084360082, 1519855964, 10367726],
    [1483712212, 1091351397, 34429812],
    [3094727808, 2186637247, 273584935],
    [1423662510, 3991222595, 60049702],
    [3808588784, 4111911476, 102622226],
    [1518142024, 2591321500, 13033199]
]

fertilizer_to_water = [
    [206818393, 1973789958, 18543481],
    [2641351404, 1992333439, 41420268],
    [58400970, 2574944960, 107826712],
    [3710426911, 4065366707, 42793360],
    [4217161704, 4274048011, 20919285],
    [1926695368, 705931711, 328031436],
    [1449580741, 1210970895, 50549447],
    [907984567, 1421828853, 15115545],
    [769748018, 1108192216, 102778679],
    [451427938, 35457870, 38201654],
    [2254726804, 2033892789, 137829519],
    [923239194, 1513967644, 270588891],
    [3753220271, 4108160067, 165887944],
    [499804857, 310274559, 109862756],
    [3061525238, 3535532059, 426476055],
    [1193828085, 73659524, 196024324],
    [872526697, 0, 35457870],
    [1766386857, 1261520342, 160308511],
    [4057593930, 3283950856, 159567774],
    [1389852409, 646203379, 59728332],
    [3919108215, 3962008114, 103358593],
    [1577153434, 1784556535, 189233423],
    [4022466808, 3443518630, 35127122],
    [489629592, 1098016951, 10175265],
    [923100112, 2033753707, 139082],
    [2392556323, 2390203683, 158894869],
    [1500130188, 1436944398, 77023246],
    [2577297600, 1033963147, 64053804],
    [609667613, 2171722308, 160080405],
    [3488001293, 3061525238, 222425618],
    [2551451192, 2549098552, 25846408],
    [4238080989, 3478645752, 56886307],
    [166227682, 269683848, 40590711],
    [0, 2331802713, 58400970],
    [225361874, 420137315, 226066064]
]

water_to_light = [
    [1833244152, 0, 764535859],
    [212138399, 2132863085, 224047237],
    [445686952, 1600446740, 163005122],
    [3322180377, 2914685303, 488586806],
    [2739726430, 3712513349, 582453947],
    [3946546331, 3589340640, 8839399],
    [1441711040, 799272484, 245821386],
    [1038755613, 1763451862, 6623730],
    [608692074, 1587251997, 13194743],
    [701103180, 2356910322, 39153476],
    [1687532426, 1045093870, 145711726],
    [2597780011, 764535859, 34736625],
    [740256656, 1490869662, 54307168],
    [0, 1920724686, 212138399],
    [2632516636, 1545176830, 9229765],
    [668257778, 1554406595, 32845402],
    [3955385730, 2739726430, 39179725],
    [4180633986, 3598180039, 114333310],
    [3810767183, 2778906155, 135779148],
    [1291061946, 1770075592, 150649094],
    [436185636, 1481368346, 9501316],
    [1045379343, 2396063798, 245682603],
    [794563824, 1237176557, 244191789],
    [621886817, 1190805596, 46370961],
    [3994565455, 3403272109, 186068531]
]

light_to_temperature = [
    [432141642, 1268486741, 19474646],
    [3617581823, 3276436954, 357008111],
    [3505110084, 3786131308, 49942802],
    [0, 1287961387, 432141642],
    [3096011130, 1808659179, 409098954],
    [1347993824, 2675880000, 161612192],
    [3019335150, 3199760974, 76675980],
    [3555052886, 3137232037, 62528937],
    [2778092757, 1720103029, 88556150],
    [451616288, 2217758133, 458121867],
    [1509606016, 0, 1268486741],
    [909738155, 3836074110, 138515824],
    [1048253979, 2837492192, 299739845],
    [2866648907, 3633445065, 152686243]
]

temperature_to_humidity = [
    [646729740, 1519504972, 559297346],
    [1894539176, 2990410634, 44298872],
    [232257988, 972432123, 414471752],
    [2277879451, 278205785, 108711195],
    [1775790220, 132298732, 118748956],
    [3371687162, 2663455233, 326955401],
    [1612056920, 272509895, 5695890],
    [1208383109, 3703499740, 147415518],
    [4070380190, 4053129082, 69974785],
    [4155541210, 3305585510, 139426086],
    [81956384, 386916980, 150301604],
    [3987543096, 896459472, 75972651],
    [2148980475, 1386903875, 128898976],
    [1617752810, 3445011596, 154599732],
    [4063515747, 2078802318, 6864443],
    [2392568787, 3599611328, 101532389],
    [2386590646, 4123103867, 5978141],
    [2494101176, 2122546980, 187027686],
    [2681128862, 2085666761, 36880219],
    [4140354975, 2648268998, 15186235],
    [1772352542, 3051742077, 3437678],
    [1355798627, 3850915258, 202213824],
    [3720104770, 3055179755, 250405755],
    [3032992830, 2309574666, 338694332],
    [1206027086, 3701143717, 2356023],
    [1938838048, 537218584, 44257139],
    [1558012451, 81956384, 50342348],
    [3970510525, 3034709506, 17032571],
    [1608354799, 1515802851, 3702121],
    [1983095187, 4129082008, 165885288],
    [3698642563, 251047688, 21462207],
    [2718009081, 581475723, 314983749]
]

humidity_to_location = [
    [971626884, 4275486551, 19480745],
    [1218249913, 2090555906, 502249162],
    [2914848039, 2902831882, 224865747],
    [3341591733, 2819947352, 82884530],
    [991107629, 2592805068, 227142284],
    [3424476263, 606585628, 95279547],
    [4279176998, 2064757318, 10971709],
    [3139713786, 4068790015, 201877947],
    [606585628, 701865175, 365041256],
    [3534582689, 3291885426, 744594309],
    [1916997152, 1066906431, 997850887],
    [1752809355, 3127697629, 164187797],
    [1720499075, 4036479735, 32310280],
    [4290148707, 4270667962, 4818589],
    [3519755810, 2075729027, 14826879]
]


output = []
for num in seeds:
    output.append(recurrsion(num))

print(min(output))
