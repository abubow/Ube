# import os
# import django

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ube.settings')
# django.setup()

# from base.models import Topic

# # List of philosophy topics (from #10 onwards) with descriptions
# topics = [
#     {
#         'name': 'Analytic Philosophy',
#         'description': 'A style of philosophy that emphasizes clarity, precision, and logical analysis of language and concepts.'
#     },
#     {
#         'name': 'Continental Philosophy',
#         'description': 'A diverse set of 19th- and 20th-century philosophical traditions from mainland Europe, including existentialism, phenomenology, and deconstruction.'
#     },
#     {
#         'name': 'Philosophy of Language',
#         'description': 'The study of the nature, origins, and usage of language, and the relationship between language and reality.'
#     },
#     {
#         'name': 'Philosophy of Science',
#         'description': 'The exploration of the methods, foundations, and implications of science, including scientific explanation and theory.'
#     },
#     {
#         'name': 'Philosophy of Religion',
#         'description': 'The examination of religious beliefs, practices, and the nature and existence of the divine.'
#     },
#     {
#         'name': 'Hermeneutics',
#         'description': 'The study of interpretation, especially of texts, and the understanding of meaning in language.'
#     },
#     {
#         'name': 'Pragmatism',
#         'description': 'A philosophical tradition that emphasizes the practical application of ideas and the role of experience in shaping beliefs.'
#     },
#     {
#         'name': 'Stoicism',
#         'description': 'An ancient Greek and Roman philosophy that teaches the development of self-control and fortitude to overcome destructive emotions.'
#     },
#     {
#         'name': 'Utilitarianism',
#         'description': 'An ethical theory that advocates for actions that maximize happiness and well-being for the greatest number of people.'
#     },
#     {
#         'name': 'Deontology',
#         'description': 'An ethical theory that emphasizes the importance of rules, duties, and obligations in determining moral action.'
#     },
#     {
#         'name': 'Virtue Ethics',
#         'description': 'An ethical approach that focuses on the development of good character traits (virtues) and the pursuit of moral excellence.'
#     },
#     {
#         'name': 'Feminist Philosophy',
#         'description': 'The exploration of issues related to gender, inequality, and the critique of traditional philosophical perspectives from a feminist standpoint.'
#     },
#     {
#         'name': 'Critical Theory',
#         'description': 'A social and political philosophy that critiques and seeks to transform society by addressing power structures and inequalities.'
#     },
#     {
#         'name': 'Environmental Philosophy',
#         'description': 'The study of the ethical, political, and metaphysical issues related to the environment and human interaction with the natural world.'
#     },
#     {
#         'name': 'Bioethics',
#         'description': 'The examination of ethical issues in the fields of medical and biological sciences, including topics like medical treatment, genetics, and biotechnology.'
#     },
#     {
#         'name': 'Eastern Philosophy',
#         'description': 'Philosophical traditions and schools of thought originating in East and South Asia, including Confucianism, Taoism, Buddhism, and Hinduism.'
#     }
# ]

# # Add topics to the database
# for topic in topics:
#     Topic.objects.get_or_create(name=topic['name'], defaults={'description': topic['description'], 'link': topic['name'].replace(' ', '').lower()})

# print("Topics added to the database successfully.")

import os
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ube.settings')
django.setup()

from base.models import Room, Topic, User

# Function to generate a unique link for each room based on its name
def generate_unique_link(name):
    return slugify(name)[:50]

# List of room names, descriptions, and topics
rooms_data = [
    {
        'name': 'Philosophical Discourse Hub',
        'description': 'A place to engage in deep discussions on Analytic Philosophy, Continental Philosophy, and the Philosophy of Language.',
        'topics': ['Analytic Philosophy', 'Continental Philosophy', 'Philosophy of Language']
    },
    {
        'name': 'Scientific and Religious Dialogues',
        'description': 'Exploring the intersections of science and religion through philosophical inquiry.',
        'topics': ['Philosophy of Science', 'Philosophy of Religion']
    },
    {
        'name': 'Interpretation and Practical Wisdom',
        'description': 'Delving into Hermeneutics and Pragmatism to understand and apply philosophical concepts in real life.',
        'topics': ['Hermeneutics', 'Pragmatism']
    },
    {
        'name': 'Ethical Living and Stoic Virtues',
        'description': 'Discussing ethical theories and Stoicism to cultivate moral and virtuous living.',
        'topics': ['Utilitarianism', 'Deontology', 'Virtue Ethics', 'Stoicism']
    },
    {
        'name': 'Critical and Eastern Perspectives',
        'description': 'Engaging with critical theory, feminist philosophy, and Eastern philosophical traditions to broaden our understanding of the world.',
        'topics': ['Critical Theory', 'Feminist Philosophy', 'Eastern Philosophy']
    }
]

# Fetch the user who will be the host
host_user = User.objects.get(email='smabuzar00@gmail.com')

# Create rooms and assign topics
for room_data in rooms_data:
    room = Room.objects.create(
        name=room_data['name'],
        description=room_data['description'],
        link=generate_unique_link(room_data['name']),
        host=host_user
    )
    for topic_name in room_data['topics']:
        topic = Topic.objects.get(name=topic_name)
        room.topics.add(topic)
    room.save()

print("Rooms added to the database successfully.")
