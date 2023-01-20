musicstyle=["Hip hop","Rock","Reggae","country"]
musicdescription=[
"hip-hop music, also known as rap music, is a genre of popular music developed in the United States by inner-city African Americans, Caribbean Americans and Latino Americans in the Bronx borough of New York City in the 1970s.",
"rock music characterized by a strong beat, the use of blues forms and the presence of rock instruments such as electric guitar, electric bass, electric organ or electric piano.",
"raggie is popular music of Jamaican origin that combines native styles with elements of rock and soul music and is performed at moderate tempos with the accent on the offbeat",
"Country is a genre of popular music that originated with blues, church music such as Southern gospel and spirituals, old-time, and American folk music forms"]
print("which style of music you want to hear from us?")
for i in range(5):
    option=int(input("type 1 for hip hop 2 for rock 3 for raggie 4 for country\n"))
    if option>4:
        print("please choose option between 1 to 4")
    else:
        print("you have opted for",musicstyle[option-1])
        print(musicdescription[option-1])
        break 
if i >= 4:
    print("you have exceeded the total number of tries")













