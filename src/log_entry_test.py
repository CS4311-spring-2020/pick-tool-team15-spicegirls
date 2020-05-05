import log_entry
from bson import ObjectId

for x in range(1, 11):
    print(log_entry.create_log_entry("Content", "10:20:20:10:10", "host", "red", "sourceType"))


print(log_entry.change_log_entry_content("5eb12bfa61b2f7cd8aac1c4d", "New Content"))

print(log_entry.change_log_entry_timestamp("5eb12bfa61b2f7cd8aac1c4d", "10:20:20:10:13"))

print(log_entry.change_log_entry_host("5eb12bfa61b2f7cd8aac1c4d", "New Host"))

print(log_entry.change_log_entry_source("5eb12bfa61b2f7cd8aac1c4d", "New Source"))

print(log_entry.change_log_entry_source_type("5eb12bfa61b2f7cd8aac1c4d", "New Source Type"))

#print(log_entry.delete_log_entry("5eb12bfa61b2f7cd8aac1c4c"))

