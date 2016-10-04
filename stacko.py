
# for comment in comments:
#     print(comment) # was missing parens in call to 'print'
#     if comment == None:
#         flag=+1
#         if flag==1:
#             row += 1
#     if comment != None:
#         flag=0
#         if comment.find('of') != -1:
#             countC = comment.split("of ")
#             countCC = int(re.sub("\D", "", countC[1]))
#         else:
#             countCC = comment
#         try:
#             worksheet.write(row, 4, "Komentarzy:")
#             worksheet.write(row, 5, countCC)
#             row += 1
#         except Exception:
#             pass




if n == '+':
    return num1 + num2

elif n == '-':
    return num1 - num2

elif n == 'x':
    return num1 * num2

elif n == '/':
    return num1 / num2
