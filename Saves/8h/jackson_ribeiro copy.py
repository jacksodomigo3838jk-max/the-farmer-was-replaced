change_hat(Hats.Purple_Hat)
do_a_flip()
while 1:
	if can_harvest():
		harvest()            
       move(North) # type: ignore
do_a_flip()