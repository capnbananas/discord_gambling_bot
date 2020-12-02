import os, json, random
from PIL import Image, ImageFont

#----------------------------------------------------------------------------------------------------

slot1 = Image.open('games/images/1.png')
slot2 = Image.open('games/images/2.png')
slot3 = Image.open('games/images/3.png')
slot4 = Image.open('games/images/4.png')
slot5 = Image.open('games/images/5.png')
slot6 = Image.open('games/images/6.png')
blank = Image.open('games/images/slot_blank.png')

def spin():
	results = []
	i = 0
	while len(results) < 3:
		results.append(slot_range())
	return results

def slot_range():
	if bonus_range() == 3:
		return 5
	else:
		out = random.randrange(5)
		return out

def bonus_range():
	out = random.randrange(5)
	if out == 3:
		return out
	else:
		pass

def check(list):
    return all(i == list[0] for i in list)

def slot_machine(ammount):
	tbt = []
	pool = []
	i = 0

	while i < 3:
		i += 1
		result = spin()
		tbt.append(result)

	update_pos(tbt)
	top_line = tbt[0]
	mid_ling = tbt[1]
	bot_line = tbt[2]
	vertical1 = [top_line[0], mid_ling[1], bot_line[2]]
	vertical2 = [bot_line[0], mid_ling[1], top_line[2]]
	wager_lines = [top_line, mid_ling, bot_line, vertical1, vertical2]

	for line in wager_lines:
		if line[0] == 5:
			print(line[1], line[2])
		check_winning = check(line)

		if bool(check_winning) is True:
			pool.append(win_option(ammount, line[0]))
	return pool

def update_pos(results):
	pos1(results[0][0])
	pos2(results[0][1])
	pos3(results[0][2])
	pos4(results[1][0])
	pos5(results[1][1])
	pos6(results[1][2])
	pos7(results[2][0])
	pos8(results[2][1])
	pos9(results[2][2])

def win_option(ammount, option):
	if option == 0:
		payout1 = 2 * ammount
		print(payout1)
		return payout1
	if option == 1:
		payout2 = 4 * ammount
		print(payout2)
		return payout2
	if option == 2:
		payout3 = 8 * ammount
		print(payout3)
		return payout3
	if option == 3:
		payout4 = 16 * ammount
		print(payout4)
		return payout4
	if option == 4:
		payout5 = 32 * ammount
		print(payout5)
		return payout5
	if option == 5:
		payout6 = 64 * ammount
		print(payout6)
		return payout6

#----------------------------------------------------------------------------------------------------
def pos1(result):
	if result == 0:
		blank.paste(slot1, (0, 285))
		blank.save('games/images/slot_output.png')
	if result == 1:
		blank.paste(slot2, (0, 285))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (0, 285))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (0, 285))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (0, 285))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (0, 285))
		blank.save('games/images/slot_output.png')		

def pos2(result):
	if result == 0:
		blank.paste(slot1, (170, 285))
		blank.save('games/images/slot_output.png')	
	if result == 1:
		blank.paste(slot2, (170, 285))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (170, 285))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (170, 285))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (170, 285))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (170, 285))
		blank.save('games/images/slot_output.png')

def pos3(result):
	if result == 0:
		blank.paste(slot1, (330, 285))
		blank.save('games/images/slot_output.png')	
	if result == 1:
		blank.paste(slot2, (330, 285))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (330, 285))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (330, 285))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (330, 285))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (330, 285))
		blank.save('games/images/slot_output.png')

#----------------------------------------------------------------------------------------------------
def pos4(result):
	if result == 0:
		blank.paste(slot1, (0, 440))
		blank.save('games/images/slot_output.png')
	if result == 1:
		blank.paste(slot1, (0, 440))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot2, (0, 440))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot3, (0, 440))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot4, (0, 440))
		blank.save('games/images/slot_output.png')	
	if result == 5:
		blank.paste(slot6, (0, 440))
		blank.save('games/images/slot_output.png')	

def pos5(result):
	if result == 0:
		blank.paste(slot1, (170, 440))
		blank.save('games/images/slot_output.png')	
	if result == 1:
		blank.paste(slot2, (170, 440))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (170, 440))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (170, 440))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (170, 440))
		blank.save('games/images/slot_output.png')	
	if result == 5:
		blank.paste(slot6, (170, 440))
		blank.save('games/images/slot_output.png')					

def pos6(result):
	if result == 0:
		blank.paste(slot1, (330, 440))
		blank.save('games/images/slot_output.png')	
	if result == 1:
		blank.paste(slot2, (330, 440))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (330, 440))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (330, 440))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (330, 440))
		blank.save('games/images/slot_output.png')		
	if result == 5:
		blank.paste(slot6, (330, 440))
		blank.save('games/images/slot_output.png')	

#----------------------------------------------------------------------------------------------------
def pos7(result):
	if result == 0:
		blank.paste(slot1, (0, 570))
		blank.save('games/images/slot_output.png')
	if result == 1:
		blank.paste(slot2, (0, 570))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (0, 570))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (0, 570))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (0, 570))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (0, 570))
		blank.save('games/images/slot_output.png')	

def pos8(result):
	if result == 0:
		blank.paste(slot1, (170, 570))
		blank.save('games/images/slot_output.png')
	if result == 1:
		blank.paste(slot2, (170, 570))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (170, 570))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (170, 570))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (170, 570))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (170, 570))
		blank.save('games/images/slot_output.png')	

def pos9(result):
	if result == 0:
		blank.paste(slot1, (330, 570))
		blank.save('games/images/slot_output.png')	
	if result == 1:
		blank.paste(slot2, (330, 570))
		blank.save('games/images/slot_output.png')
	if result == 2:
		blank.paste(slot3, (330, 570))
		blank.save('games/images/slot_output.png')
	if result == 3:
		blank.paste(slot4, (330, 570))
		blank.save('games/images/slot_output.png')
	if result == 4:
		blank.paste(slot5, (330, 570))
		blank.save('games/images/slot_output.png')
	if result == 5:
		blank.paste(slot6, (330, 570))
		blank.save('games/images/slot_output.png')	