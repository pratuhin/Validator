import collections
from pathlib import Path
import json
import os
import designer
from collections import Counter
import operator as op
c_section = json.loads(input("Insert the Sections JSON Code - "))
c_questions = json.loads(input("Insert the Questions JSON Code - "))


def current_question_data():
    f_name = "issues.txt"
    output = Path(f_name)
    global c_questions, c_section
    if output.is_file():
        print("Deleting Previous Output txt file.")
        os.remove(f'{f_name}')
        os.system(f'type nul > {f_name}')
    c_question_group_bucket_duplicate = []
    duplicated_answer_ids = []
    c_question_group_bucket = []
    sections_id_bucket = []
    mandates = []
    q_group_ids = []
    duplicated_question_group_id = []
    for values, data in c_questions.items():
        if values not in q_group_ids:
            q_group_ids.append(values)
        else:
            duplicated_question_group_id.append(values)

    for values, data in c_section.items():
        sections_id_bucket.append(values)
        if "workflow_question_group_ids" in data:
            number_of_mandates = len(data["workflow_question_group_ids"])
            for n in range(0, number_of_mandates):
                mandates.append(data['workflow_question_group_ids'][n])

    # ---------------*************----------------
    follow_up_bucket = []
    q_groups_with_no_parent = []
    c_question_id_bucket = []
    c_answer_id_bucket = []
    auto_answer = []
    jumps_used = []
    wrong_jumps = []
    mandate_not_found = []
    for c_group_id, c_data in c_questions.items():
        c_question_group_bucket.append(c_group_id)
        # else:
        #     duplicated_question_group_id.append(c_group_id)
        c_length_of_questions = len(c_data["workflow_questions"])
        for x in range(0, c_length_of_questions):
            c_question_group_counter = c_group_id
            c_counter = 0
            if "radio_options" in c_data["workflow_questions"][x]["responses"][0]:
                c_length_of_answers = len(c_data["workflow_questions"][x]["responses"][0]["radio_options"])
            elif "checkbox_options" in c_data["workflow_questions"][x]["responses"][0]:
                c_length_of_answers = len(c_data["workflow_questions"][x]["responses"][0]["checkbox_options"])
            else:
                c_length_of_answers = 1
            c_question_ids = c_data["workflow_questions"][x]["id"]
            c_question_id_bucket.append(c_question_ids)
            for i in range(0, c_length_of_answers):
                if "radio_options" in c_data["workflow_questions"][x]["responses"][0]:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]["id"]
                    if "followup_question_group_ids" in c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]:
                        length_of_followups = len(c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]["followup_question_group_ids"])
                        for t in range(0, length_of_followups):
                            follow_ups = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]["followup_question_group_ids"][t]
                            if follow_ups not in follow_up_bucket:
                                follow_up_bucket.append(follow_ups)
                    if "next_node_override" in c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]:
                        jump = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]["next_node_override"]
                        jumps_used.append(c_answer_ids)
                        if jump not in sections_id_bucket:
                            wrong_jumps.append(c_answer_ids)
                elif "checkbox_options" in c_data["workflow_questions"][x]["responses"][0]:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["checkbox_options"][c_counter]["id"]
                else:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["id"]
                if c_answer_ids not in c_answer_id_bucket:
                    c_answer_id_bucket.append(c_answer_ids)
                else:
                    duplicated_answer_ids.append(c_answer_ids)
                if c_question_group_counter == c_group_id:
                    c_counter += 1
                else:
                    c_counter = 0
                i += 1
            if "answer_eval_attributes" in c_data["workflow_questions"][x]:
                auto_answer.append(c_group_id)
            x += 1
        if c_group_id not in duplicated_question_group_id:
            duplicated_question_group_id.append(c_group_id)
    # duplicate_list = follow_up_bucket
    # follow_up_bucket = []
    #
    # for items in duplicate_list:
    #     if items not in follow_up_bucket and items != '':
    #         follow_up_bucket.append(items)

    for items in follow_up_bucket:
        if items not in c_question_group_bucket:
            print("\nFollow up " + items + " not available.\n", file=open(f_name, "a"))

    for items in c_question_group_bucket:
        if items not in follow_up_bucket:
            if items not in mandates:
                q_groups_with_no_parent.append(items)

    if len(jumps_used) > 0:
        print("\nAnswers using Jumps - ", jumps_used, file=open(f_name, "a"))

    if len(wrong_jumps) > 0:
        print("\nAnswers using wrong jumps - ", wrong_jumps, file=open(f_name, "a"))

    if len(q_groups_with_no_parent) > 0:
        print("\nInactive question groups - ", q_groups_with_no_parent, file=open(f_name, "a"))

    # Checking if mandates from sections.json are present in the questions.json file.

    for items in mandates:
        if items not in c_question_group_bucket:
            mandate_not_found.append(items)

    if len(mandate_not_found) > 0:
        print("Mandate(s) not found in the questions json - ", mandate_not_found, file=open(f_name, "a"))

    if len(duplicated_answer_ids) > 0:
        print("Duplicate answer ids - ", duplicated_answer_ids, file=open(f_name, "a"))

    wrong_answer_ids = []
    for answers in c_answer_id_bucket:
        if answers.startswith("Q-"):
            wrong_answer_ids.append(answers)
    if len(wrong_answer_ids) > 0:
        print("Answer ID that starts with Q- ", wrong_answer_ids, file=open(f_name, "a"))
    if len(auto_answer) > 0:
        print("Questions using auto-answers : ", auto_answer, file=open(f_name, "a"))


def clean_code():
    global c_questions, c_section
    mandates = []
    starting_section = input("Please enter the starting section : ")
    for node_id, data in c_section:
        if starting_section == node_id:
            number_of_mandates = len(data["workflow_question_group_ids"])
            for n in range(0, number_of_mandates):
                mandates.append(data['workflow_question_group_ids'][n])
        if "next_workflow_node" in data:
            next_section = data["next_workflow_node"]


current_question_data()
