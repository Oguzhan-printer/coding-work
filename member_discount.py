
identity = str(input('Are you a member or not? (member/non-member): '))
shop = int(input('Enter your shopping amount: '))

if identity == 'member':
    print(f'Congratulations, you have won a 10% {shop - (shop%10)} discount.')
elif identity == 'non-member':
    print(f'Congratulations, you have won a 10% {shop - (shop%5)} discount.')
else:
    print('Invalid input. Please enter member or non-member.')
