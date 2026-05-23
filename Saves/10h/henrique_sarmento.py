change_hat(Hats.Gray_Hat)
do_a_flip()
while True:
    if can_harvest():
        harvest()
        
    move(North)
    if can_harvest():
        harvest()

    move(North)
    if can_harvest():
        harvest()

    plant(Entities.Bush)
    move(North)