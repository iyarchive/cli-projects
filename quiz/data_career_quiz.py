#defining a node
class Node:
    def __init__(self, question=None, options=None, result=None):
        self.question = question
        self.options = options or {}
        self.result = result

#results nodes
data_analyst = Node(result={
    "role": "Data Analyst",
    "skills": ["Excel/Sheets", "SQL", "Python", "PowerBI",
               "Statistics", "Tableau"]
})

data_scientist = Node(result={
    "role": "Data Scientist",
    "skills": ["Python", "Statistics","Probability", "Machine Learning",
               "R", "SQL", "Linear Algebra"]
})

data_engineer = Node(result={
    "role": "Data Engineer",
    "skills": ["SQL", "Python", "Data Pipelines", "Databases",
               "Statistics", "ETL/ELT", "Cloud"]
})

ml_engineer = Node(result={
    "role": "ML Engineer",
    "skills": ["Python", "Machine Learning", "Deep Learning", "MLOps",
               "Cloud", "Statistics"]
})

ml_researcher = Node(result={
    "role": "ML Researcher",
    "skills": ["Mathematics", "Python", "Deep Learning", "Statistics",
               "Research", "Python", "R", "Machine Learning", "Linear Algebra"]
})

ai_engineer = Node(result={
    "role": "AI Engineer",
    "skills": ["Python", "APIs", "LLM Frameworks", "Prompt Engineering",
               "RAG Systems", "Vector Databases", "Machine Learning",
               "Deep Learning", "SQL", "Cloud", "Docker"]
})

#question nodes
predictive_modeling_node = Node(
    question="What part of predictive modeling interests you most?",
    options={
        "Experimenting with models and features": data_scientist,
        "Deploying models into production systems": ml_engineer
    }
)

statistical_inference_node = Node(
    question="Which type of question fascinates you more?",
    options={
        "Whether patterns are statistically meaningful": data_scientist,
        "Whether learning algorithms can be improved": ml_researcher,
        "How to make ML systems perform reliably in real-world environments": ml_engineer
    }
)

predictive_stats_node = Node(
    question="Which sounds more exciting long-term?",
    options={
        "Using models to solve practical problems": data_scientist,
        "Understanding the theory behind intelligent systems": ml_researcher
    }
)

pattern_node = Node(
    question="When you find a pattern, what do you want to do next?",
    options={
        "Explain it clearly to people": data_analyst,
        "Test if it predicts future outcomes": predictive_modeling_node,
        "Question whether the pattern is statistically real": statistical_inference_node,
        "Both prediction and statistical validity": predictive_stats_node
    }
)

systems_node = Node(
    question="Which problem sounds more satisfying to solve?",
    options={
        "Data is scattered, broken, and needs a reliable pipeline": data_engineer,
        "A model works in a notebook but needs to run in the real world": ml_engineer
    }
)

theory_node = Node(
    question="What part of intelligent systems fascinates you the most?",
    options={
        "Building AI products people can actually use": ai_engineer,
        "Training and deploying machine learning systems": ml_engineer,
        "Understanding and improving how learning algorithms work": ml_researcher
    }
)

hybrid_node = Node(
    question="If everything interests you, what would you rather be known first?",
    options={
        "The person who builds AI products": ai_engineer,
        "The person who advances the science behind ML": ml_researcher,
        "The person who wants to understand intelligence itself": ml_researcher,
        "The person who finds meaning inside overwhelming information": pattern_node,
        "The person that creates machines that can adapt and improve": ml_engineer,
        "The person who improves how machines learn": theory_node,
        "The person who makes large systems stable, efficient, and scalable": systems_node
    }
)

#root node
root = Node(
    question="What naturally catches your curiosity?",
    options={
        "Finding patterns in messy data": pattern_node,
        "Building reliable systems": systems_node,
        "Teaching machines to learn": theory_node,
        "All of them": hybrid_node
    }
)

current_node = root

#making the questionnaire
print("🌸 Data Skills Prioritizer 🌸")

while current_node.result is None:
    print("\n" + current_node.question)

    choices = list(current_node.options.keys())

    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")

    answer = input("Choose a number: ").strip()

    if answer.isdigit():
        answer = int(answer)

        if 1 <= answer <= len(choices):
            selected_option = choices[answer - 1]
            current_node = current_node.options[selected_option]
        else:
            print("Invalid number.")
    else:
        print("Please enter a number.")


print("\n✨ Your recommended path:")
print(current_node.result["role"])

print("\nSkills to learn:")
for i, skill in enumerate(current_node.result["skills"], start=1):
    print(f"{i}. {skill}")
