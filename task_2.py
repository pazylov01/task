new_list = 'Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless.But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'

new_list_2 = new_list.lower()
c = 0
x = 0

for i in new_list_2:
    if i == 't':
        c += 1
    if i == 's':    
        x += 1
print(c, x)


list_of_adverts = ''


for item in new_list_2:
    if item == 'advert':
        qwerty = item.replace('advert', 'ADVERT')
        list_of_adverts.append(qwerty)
        
print((list_of_adverts))        
