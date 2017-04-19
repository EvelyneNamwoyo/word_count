def words(word):
	sword=word.split()
	word_dict={}
	for i in sword:
		if i.isdigit():
			i=int(i)
		if i in word_dict:
 			word_dict[i]+=1
		else:
			word_dict[i]=1


# def words(word):
# 	if '\n' in word:
# 		sword=word.split('\n')
# 	elif '\t' in word:
# 		sword=word.split('\t')
# 	else:

# 		sword=word.split(' ')
	
# 	word_dict={}
# 	for i in sword:
# 		if i.isdigit():
# 			i=int(i)
# 		if i in word_dict:
# 			word_dict[i]+=1
# 		else:
# 			word_dict[i]=1
# 	for i in word_dict:
# 		if i.isdigit():
# 			int(i)


	
	return word_dict
print (words ('1 3 2 5'))
