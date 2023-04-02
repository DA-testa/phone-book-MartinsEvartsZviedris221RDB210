class Query:
def init(self, query):
self.type = query[0]
self.number = int(query[1])
if self.type == 'add':
self.name = query[2]

def read_queries():
n = int(input())
return [Query(input().split()) for i in range(n)]

def write_responses(result):
print('\n'.join(result))

def process_queries(queries):
result = []
# Use a hash map to store the contacts, with the number as the key
contacts = {}
for cur_query in queries:
if cur_query.type == 'add':
# add or overwrite a contact with this number
contacts[cur_query.number] = cur_query.name
elif cur_query.type == 'del':
# remove a contact with this number, if it exists
contacts.pop(cur_query.number, None)
else:
# look up the contact with this number, or return "not found"
result.append(contacts.get(cur_query.number, "not found"))
return result

if name == 'main':
write_responses(process_queries(read_queries()))
