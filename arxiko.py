# Pick up number app

print(input('Καλως ηρθατε στην εφαρμογη Pick Up Her Number!!!'))
print('')
print(input('Στην εφαρμογη θα χρειαστουμε μονο τα τελευταια 7 ψηφια του αριθμου, δεν χρειαζομαστε τον παροχο(Cosmote,'#Introducing the app
      'Vodafone,Wind etc...).'))
print('')
print("Παρολ' ταυτα θα ρωτησουμε με ενα τροπο χιουμοριστικα. Βρες το μονο σου!!! :) xD")


print ('Ποια ειναι  τα πρωτα 3 ψηφια μετα τον παροχο...')# Askinf for the first 3 digits after the provider(vodafone etc...)
next3Digits = (input(int()))
while len(next3Digits) > 3:
    next3Digits = (input('Give 3 numbers: '))
    if len(next3Digits) == 3:
        break

print('Και πολλαπληασετα με το 80...')# Multiply by 80
mult = (int(next3Digits) * 80)
addit = (int(mult + 1))
sec_mult = (int(addit) * 250)
print(sec_mult)

print('Προσθεσε τα τελευταια 4 ψηφια του αριθμου σου...') # Add the last 4 digits from your number
last4Digits = (input(int()))
while len(last4Digits) != 4:
    last4Digits = (input('Give 4 numbers: '))
    if len(last4Digits) == 4:
            break

add_sec = (int(sec_mult) + int(last4Digits))
print(add_sec)
print('Ξανα προσθεσε τα τελευταια 4 ψηφια...') # Add again the last 4 digits
repeat = (input(int()))
result = ((int(repeat) + int(add_sec)))
print(result)
print('Αφαιρεσε 250 απο το αποτελεσμα....') # Substract 250 from the result
print(input())
sub = (int(result) - 250)
print(sub)
print('Τελος διαιρεσετα ολα δια του 2.. ')# divide the result by 2
print(input())
divid = (int(sub) // 2)
print(divid)

COSMOTE = 697
VODAFONE = 694
WIND = 693
print('Ποιος ειναι ο παροχος σου....')# Who is your provider 
answer = input()
if answer == 'cosmote':
    first3digits = COSMOTE
elif answer == 'vodafone':
    first3digits = VODAFONE
elif answer == 'wind':

    first3digits = WIND

first3digits1 = str(first3digits)

print('Ο αριθμος σου ειναι ', first3digits1,'-', divid) # Your phone number is ....





