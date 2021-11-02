n = int(input())
post = input().split(' опубликовал пост, количество просмотров: ')
pop = {post[0]: [int(post[-1]), 'origin']}
for _ in range(n - 1):
    post = input()
    repost, post = post.split(' отрепостил пост у ')
    author, views = post.split(', количество просмотров: ')
    pop[repost] = [int(views), author]
    while author != 'origin':
        pop[author][0] += int(views)
        author = pop[author][1]
for val in pop.values():
    print(val[0])