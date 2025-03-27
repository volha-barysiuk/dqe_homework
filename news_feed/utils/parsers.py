from news_feed.configs import NEWS, PRIVATE_AD, RUMOR

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


# Function parses a post list retrieved from JSON file.
# Parameter: raw_post_list (list): List with posts retrieved from JSON file.
# Returns: list of data required to create a new post (post type, text, end line specific for each post type)
def parse_posts_from_json(raw_post_list):
    posts_list = []
    end_line_dict = {
        NEWS: 'city',
        PRIVATE_AD: 'expiryDate',
        RUMOR: 'celebrity'
    }
    if not raw_post_list:
        raise ValueError('JSON file should include at least one post.')
    for post in raw_post_list:
        posts_list.append([post.get('type'),
                           post.get('text'),
                           post.get(end_line_dict.get(post.get('type', ''), ''), '')])
    return posts_list