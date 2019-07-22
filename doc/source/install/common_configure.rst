2. Edit the ``/etc/freecell_solver/freecell_solver.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://freecell_solver:FREECELL_SOLVER_DBPASS@controller/freecell_solver
