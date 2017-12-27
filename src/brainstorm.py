#Brain storming data structures and functions
problem = {}
    #id:[problem text, solution text, workspace text]
    #function to add new exercise, assigning unique id (integer)
    #problem(id)[0] returns text for the problem, [1] solution, [2] workspace]

DBsection = {}
    #section:[id1, id2, ...]
    #DBsection(section) returns list of problem ids

problem_meta = {}
    #id: (calc_type, difficulty, level, source) named tuple
    #calc_type: 0 no calculator allowed, 1 allowed, 2 calc practice
    #difficulty 1-10
    #level 1-6 (webworks reference)
    #source - author, or history of exercise ("cjh")

problem_set = {}
    #set_id:(problem_ids, string), text composing problems in TeX format

make_set(problem_ids, pflag, sflag, wflag, numflag)
    #function to create string of problems in TeX format
    #ids is a list of problem ids, order is maintained
    #flags specify inclusion of problem text, solution & workspace
    #numflag: 1 prefix w "\item", 2 include "\begin{enumerate}"

assignment = (date, learner_id, set_id)
    #record of assignments (tuple)

problem_hist = {}
    #id:(assigned_date, learner)
    #tracks whether and when a problem has been used

standard = {}
    #source:[tree] problem hierarchy by standard-setting authority
    #source - ccss, ibqb, jmap, deltamath, webworks
    #webworks tree is [DBcourse, [DBchapter, [DBsection1, sect2,...]]]

learner = {}
    #id:(last, first, cohort)

learner_history = {}
    #learner_id:[(problem_id, date, correct), ...] history of solved problems
    #correct is a value 0-1
