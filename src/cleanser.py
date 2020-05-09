import re


class Cleanser():
    def cleanse(file):
        if file:
            lines = open(file, encoding='utf_8').readlines()
            apache = [re.findall(r'\[(\d{2})/([a-zA-Z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2})]', line) for line in lines]
            valid = []
            if apache:
                for timestamp in apache:
                    for day, month, year, hour, min, sec in timestamp:
                        valid.append(month + ' ' + day + ' ' + year + ' ' + hour + ':' + min + ':' + sec)
            lines = [re.sub(r'[\x7f\x80]','',line) for line in lines]
            # lines = [re.sub(r'[^\$A-Za-z0-9.: /-\-\n\|\|]+', '', line) for line in lines]
            # not sure what this is for         ^^^^
            if len(valid) > 0:
                lines = [re.sub(r'(\d{1,3})\.(\d{1,3})\.(d{1,3})\.(\d{1,3})', ' ', line) for line in lines]
                lines = [re.subr('\[(\d{2})/([a-zA-Z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2})]', valid[i], lines[i]) for i in range(len(lines))]
            with open(file, 'w') as f:
                f.writelines(line for line in lines if line.strip())
                f.truncate()
            return True