
class StudentClass:
    def __init__(this, name : str):
        this.name = name
        this.grade_level = 1
    def introduce(this):
        return this.name + ", your grade level is " + str(this.grade_level)

    def promote(this):
        if this.grade_level < 12: this.grade_level += 1

    def has_passed(this, score):
        if score < 0 or score > 100:
            raise ValueError("Wrong score")
        return score >= 50

    def update_name(this, new_name):
        this.name = new_name

    def is_graduating(this):
        return this.grade_level == 12

