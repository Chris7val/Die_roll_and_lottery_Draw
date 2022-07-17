# class Die:
#
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll_die(self, number_of_rolls):
#         from random import randint
#         while number_of_rolls > 0:
#             print(randint(1, self.sides))
#             number_of_rolls = number_of_rolls - 1
#
#
# dice0 = Die(17)
# dice1 = Die(10)
# dice2 = Die(20)
# # dice0.roll_die(10)
# dice0.roll_die(3)

# from random import choice
#
#
# def get_winner_ticket(lottery_lists):
#     lottery_winner_ticket = []
#     while len(lottery_winner_ticket) < 4:
#         num = choice(lottery_lists)
#         if num not in lottery_winner_ticket:
#             lottery_winner_ticket.append(num)
#     return lottery_winner_ticket
#
#
# def print_winner_ticket(lottery_winner_ticket):
#     print("Any ticket matching these four numbers and letters wins a prize")
#     for winner in lottery_winner_ticket:
#         print(f"{winner}")
#
#
# def get_my_ticket(lottery_lists):
#     my_tickets = []
#     while len(my_tickets) < 4:
#         num = choice(lottery_lists)
#         if num not in my_tickets:
#             my_tickets.append(num)
#     return my_tickets
#
#
# def check_my_ticket(played_ticket, winning_ticket):
#     for val in played_ticket:
#         if val not in winning_ticket:
#             return False
#     return True
#
#
# lottery_list = [1, 12, 43, 16, 32, 52, 15, 13, 42, 76, 'a', 't', 'w', 'g', 'j']
# lottery_winner = get_winner_ticket(lottery_list)
# print_winner_ticket(lottery_winner)
# my_ticket = []
# num_of_loops = 0
# won = False
# while not won:
#     my_ticket = get_my_ticket(lottery_list)
#     won = check_my_ticket(my_ticket, lottery_winner)
#     num_of_loops += 1
#
# if won:
#     print(f"we have a winning ticket {my_ticket}"
#           f"\nit only took {num_of_loops} tries")
