import set5qn2

print('The Post data contains :', set5qn2.post_detail(),'\n')
[print(i) for i in set5qn2.post_get()]
[print(i) for i in set5qn2.post_bsd_user(int(input('\nEnter the required UserId :')))]

[print(i) for i in set5qn2.comment_get()]
[print(i) for i in  set5qn2.comment_bsd_post(int(input('\nEnter the required postId :')))]