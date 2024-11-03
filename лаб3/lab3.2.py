# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
   set_group1 = set(group1.split(separator))
   list_group2 = group2.split(separator)
   common_set = set_group1.intersection(list_group2)
   common_list = []
   for i in common_set:
       common_list.append(i)
   common_list.sort()
   return(common_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)



