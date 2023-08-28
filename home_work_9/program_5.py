v = 'python is good language to code'
count = {let: v.count(let) for let in set(v) if let != ' '}

print(count)
