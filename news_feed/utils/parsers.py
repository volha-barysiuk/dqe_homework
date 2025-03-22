def parse_post_list(raw_post_list):
    post_list = []
    first_lines = []
    end_lines = []
    post_type = ''
    for line in raw_post_list:
        if line.title() in ('News:\n', 'Private Ad:\n', 'Rumor:\n'):
            if first_lines or end_lines:
                post_list.append([post_type, ''.join(first_lines).rstrip(), ''.join(end_lines).rstrip()])
                first_lines = []
                end_lines = []
            post_type = line[:-2]
        elif line.strip():
            first_lines.extend(end_lines)
            end_lines = [line]
        else:
            end_lines.append(line)
    return post_list