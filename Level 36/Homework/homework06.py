def twice_as_old(dad_years_old, son_years_old):
    age_of_birth = dad_years_old - son_years_old
    twice_old = age_of_birth * 2
    if dad_years_old >= twice_old:
        return dad_years_old - twice_old
    else:
        return twice_old - dad_years_old