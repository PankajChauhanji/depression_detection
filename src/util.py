import re
def get_questions():
    questions = questions = [
        [
            "Have you been experiencing any sadness lately?",
            "I do not feel sad.",
            "I feel sad.",
            "I am sad all the time and I can't snap out of it.",
            "I am so sad and unhappy that I can't stand it."
        ],
        [
            "Have you been feeling more pessimistic about things lately?",
            "I am not particularly discouraged about the future.",
            "I feel discouraged about the future.",
            "I feel I have nothing to look forward to.",
            "I feel the future is hopeless and that things cannot improve."
        ],
        [
            "Do you feel like a failure?",
            "I do not feel like a failure.",
            "I feel I have failed more than the average person.",
            "As I look back on my life, all I can see is a lot of failures.",
            "I feel I am a complete failure as a person."
        ],
        [
            "Do you get as much satisfaction out of things as you used to?",
            "I get as much satisfaction out of things as I used to.",
            "I don't enjoy things the way I used to.",
            "I don't get real satisfaction out of anything anymore.",
            "I am dissatisfied or bored with everything."
        ],
        [
            "Do you feel guilty?",
            "I don't feel particularly guilty.",
            "I feel guilty a good part of the time.",
            "I feel quite guilty most of the time.",
            "I feel guilty all of the time."
        ],
        [
            "Do you feel you are being punished?",
            "I don't feel I am being punished.",
            "I feel I may be punished.",
            "I expect to be punished.",
            "I feel I am being punished."
        ],
        [
            "Are you disappointed in yourself?",
            "I don't feel disappointed in myself.",
            "I am disappointed in myself.",
            "I am disgusted with myself.",
            "I hate myself."
        ],
        [
            "Do you blame yourself?",
            "I don't feel I am any worse than anybody else.",
            "I am critical of myself for my weaknesses or mistakes.",
            "I blame myself all the time for my faults.",
            "I blame myself for everything bad that happens."
        ],
        [
            "Do you have thoughts of killing yourself?",
            "I don't have any thoughts of killing myself.",
            "I have thoughts of killing myself, but I would not carry them out.",
            "I would like to kill myself.",
            "I would kill myself if I had the chance."
        ],
        [
            "Do you cry?",
            "I don't cry any more than usual.",
            "I cry more now than I used to.",
            "I cry all the time now.",
            "I used to be able to cry, but now I can't cry even though I want to."
        ],
        [
            "Are you irritated?",
            "I am no more irritated by things than I ever was.",
            "I am slightly more irritated now than usual.",
            "I am quite annoyed or irritated a good deal of the time.",
            "I feel irritated all the time."
        ],
        [
            "Have you lost interest in other people?",
            "I have not lost interest in other people.",
            "I am less interested in other people than I used to be.",
            "I have lost most of my interest in other people.",
            "I have lost all of my interest in other people."
        ],
        [
            "Do you have difficulty making decisions?",
            "I make decisions about as well as I ever could.",
            "I put off making decisions more than I used to.",
            "I have greater difficulty in making decisions more than I used to.",
            "I can't make decisions at all anymore."
        ],
        [
            "Do you worry about your appearance?",
            "I don't feel that I look any worse than I used to.",
            "I am worried that I am looking old or unattractive.",
            "I feel there are permanent changes in my appearance that make me look unattractive.",
            "I believe that I look ugly."
        ],
        [
            "Can you work?",
            "I can work about as well as before.",
            "It takes an extra effort to get started at doing something.",
            "I have to push myself very hard to do anything.",
            "I can't do any work at all."
        ],
        [
            "Can you sleep?",
            "I can sleep as well as usual.",
            "I don't sleep as well as I used to.",
            "I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.",
            "I wake up several hours earlier than I used to and cannot get back to sleep."
        ],
        [
            "Are you tired?",
            "I don't get more tired than usual.",
            "I get tired more easily than I used to.",
            "I get tired from doing almost anything.",
            "I am too tired to do anything."
        ],
        [
            "How is your appetite?",
            "My appetite is no worse than usual.",
            "My appetite is not as good as it used to be.",
            "My appetite is much worse now.",
            "I have no appetite at all anymore."
        ],
        [
            "Have you lost weight?",
            "I haven't lost much weight, if any, lately.",
            "I have lost more than five pounds.",
            "I have lost more than ten pounds.",
            "I have lost more than fifteen pounds."
        ],
        [
            "Are you worried about your health?",
            "I am no more worried about my health than usual.",
            "I am worried about physical problems like aches, pains, upset stomach, or constipation.",
            "I am very worried about physical problems and it's hard to think of much else.",
            "I am so worried about my physical problems that I cannot think of anything else."
        ],
        [
            "How is your interest in sex?",
            "I have not noticed any recent change in my interest in sex.",
            "I am less interested in sex than I used to be.",
            "I have almost no interest in sex.",
            "I have lost interest in sex completely."
        ]
    ]

    return questions

# def display_plot(data):
#     import matplotlib.pyplot as plt
#     # Plotting
#     plt.figure(figsize=(8, 6))
#     plt.bar(data.keys(), data.values(), color=['blue', 'green', 'red', 'orange'])
#     plt.title('BDI Scores')
#     plt.xlabel('Score Type')
#     plt.ylabel('Score')
#     plt.ylim(0, max(data.values()) + 10)  # Adjust ylim for better visualization
#     plt.grid(True)

#     plt.savefig('static/plot.png')

def display_plot(data):
    import matplotlib.pyplot as plt

    # Define colors for bars
    colors = ['cornflowerblue', 'lightgreen', 'salmon', 'gold']

    # Plotting
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.keys(), data.values(), color=colors)

    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha='center', va='bottom')

    plt.title('BDI Scores')
    plt.xlabel('Score Type')
    plt.ylabel('Score')
    plt.ylim(0, max(data.values()) + 10)  # Adjust ylim for better visualization
    plt.grid(False)  # Remove grid lines

    # Add some padding to the x-axis
    plt.xticks(rotation=45, ha='right')

    # Save the plot
    plt.tight_layout()
    plt.savefig('static/plot.png')

    # Show the plot (optional)
    # plt.show()



def interpret_score(score):
    if score >= 1 and score <= 10:
        return "These ups and downs are considered normal"
    elif score >= 11 and score <= 16:
        return "Mild mood disturbance"
    elif score >= 17 and score <= 20:
        return "Borderline clinical depression"
    elif score >= 21 and score <= 30:
        return "Moderate depression"
    elif score >= 31 and score <= 40:
        return "Severe depression"
    elif score > 40:
        return "Extreme depression"
    else:
        return "Invalid score"

def evaluate_questions(request):
    print("hello",  request.get_data())
    b'question1=3&question2=3&question3=2&question4=3&question5=3&question6=2&question7=2&question8=3&question9=2&question10=1&question11=1&question12=1&question13=1&question14=1&question15=1&question16=1&question17=1&question18=1&question19=1&question20=1&question21=1'
    response = request.get_data()
    re_results = re.findall(rb"question\d+=[1-4]", response)
    cognitive_bdi = [13, 3, 14, 5, 6, 7, 8]
    affective_bdi = [1, 2, 4, 9, 12]
    somatic_bdi = [15, 17, 19, 20, 11, 10, 16, 18, 21]
    answers = {}
    for res in re_results:
        re_g = re.search(r'\d+=\d+', str(res))
        if re_g:
            op = re_g.group()
            op = op.split('=')
            if len(op)==2:
                answers[int(op[0])] = int(op[1])-1
    scores = {
        'cognitive_bdi_score' : 0,
        'affective_bdi_score' : 0,
        'somatic_bdi_score' : 0,
        'total_score' : 0
    }
    for key, value in answers.items():
        scores['total_score'] += value
        if key in affective_bdi:
            scores['affective_bdi_score']+= value
        elif key in cognitive_bdi:
            scores['cognitive_bdi_score'] += value
        elif key in somatic_bdi:
            scores['somatic_bdi_score'] += value

    display_plot(scores)
    # 1-10________These ups and downs are considered normal 
    # 11-16_______ Mild mood disturbance 
    # 17-20_________Borderline clinical depression 
    # 21-30_________Moderate depression 
    # 31-40_________Severe depression 
    # over 40________Extreme depression
    
    return f"Your Result: {interpret_score(score=scores['total_score'])}"