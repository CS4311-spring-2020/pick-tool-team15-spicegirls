import log_entry
from bson import ObjectId

for x in range(1, 11):
    print(log_entry.create_log_entry("Content", "10:20:20:10:10", "host", "red", "sourceType"))


print(log_entry.change_log_entry_content("5eb12bfa61b2f7cd8aac1c4d", "New Content"))

#print(log_entry.delete_log_entry("5eb12bfa61b2f7cd8aac1c4c"))

