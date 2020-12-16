Three generations of solutions.

Each next one is successively faster.

Only the last one can calculate Part 2 answer in reasonable time (18s).


    [I] storm:/g/a/a/15 (master)> time python sol.py -n 202000
    0

    ________________________________________________________
    Executed in  186.19 secs   fish           external
       usr time  185.59 secs  431.00 micros  185.59 secs
       sys time    0.31 secs  232.00 micros    0.31 secs



    [I] storm:/g/a/a/15 (master)> time python sol2.py -n 202000
    2081

    ________________________________________________________
    Executed in  122.41 secs   fish           external
       usr time  122.20 secs  345.00 micros  122.20 secs
       sys time    0.13 secs  188.00 micros    0.13 secs



    [I] storm:/g/a/a/15 (master)> time python sol3.py -n 202000
    0

    ________________________________________________________
    Executed in  210.45 millis    fish           external
       usr time  206.57 millis  287.00 micros  206.28 millis
       sys time    3.48 millis  156.00 micros    3.32 millis

