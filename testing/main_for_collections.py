def max_min_len_of_course(courses, mentors, durations) -> tuple:
    courses_list = []

    for item in zip(courses, mentors, durations):
        course_dict = {"title": item[0], "mentors": item[1], "duration": item[2]}
        courses_list.append(course_dict)

    maxes = []
    minis = []
    for indx, item in enumerate(durations):
        if item == max(durations):
            maxes.append(indx)
        elif item == min(durations):
            minis.append(indx)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"])

    for id in maxes:
        courses_max.append(courses_list[id]["title"])

    return (
        f'Самый короткий курс(ы): {", ".join(courses_min)} - {min(durations)} месяца(ев)',
        f'Самый длинный курс(ы): {", ".join(courses_max)} - {max(durations)} месяца(ев)',
    )


def ordered_sequence(courses, mentors, durations) -> list:
    courses_list = []

    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for id, item in enumerate(courses_list):
        if item["duration"] in durations_dict.keys():
            durations_dict[item["duration"]].append(id)
        else:
            durations_dict[item["duration"]] = [id]

    durations_dict = dict(sorted(durations_dict.items()))

    result = list()

    for key, value in durations_dict.items():
        for el in value:
            result.append(f'{courses_list[el].get("title")} - {key} месяцев')

    return result

def correlation(courses, mentors, durations) -> tuple:
    courses_list = []

    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)

    duration_index = []
    mcount_index = []
    
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
        mcount_index.append([len(course["mentors"]), index]) 

    sorted_duration_index = sorted(duration_index)
    sorted_mcount_index = sorted(mcount_index)

    indexes_d = [val[1] for val in sorted_duration_index]
    indexes_m = [val[1] for val in sorted_mcount_index]

    return ("Связь есть" if indexes_d == indexes_m else "Связи нет", f"Порядок курсов по длительности: {indexes_d}", f"Порядок курсов по количеству преподавателей: {indexes_m}")
