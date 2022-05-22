# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = "Ruud Gullit";
player_1 = "Marco van Basten";

goal_0 = 32
goal_1 = 54

scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
# scorers = "Ruud Gullit 32, Marco van Basten 54"

report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"
# report = "Ruud Gullit scored in the 32nd minute\nMarco van Basten scored in the 54th minute"

print(report)
# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute

player = 'Ronald Koeman'
first_name = player [:player.find (' ') ]
last_name = player [player.find (' ') :]
initial_D = first_name [0]
name_short = initial_D + '. ' + last_name
last_name_len = len(last_name)
chant = (first_name + '! ') * last_name_len
chant = chant[:-1]
# chant = "Ronald! Ronald! Ronald! Ronald! Ronald! Ronald!"
good_chant = chant [len (chant)-1] != " "

print(chant)
 