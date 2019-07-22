Prerequisites
-------------

Before you install and configure the freecell service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``freecell_solver`` database:

     .. code-block:: none

        CREATE DATABASE freecell_solver;

   * Grant proper access to the ``freecell_solver`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON freecell_solver.* TO 'freecell_solver'@'localhost' \
          IDENTIFIED BY 'FREECELL_SOLVER_DBPASS';
        GRANT ALL PRIVILEGES ON freecell_solver.* TO 'freecell_solver'@'%' \
          IDENTIFIED BY 'FREECELL_SOLVER_DBPASS';

     Replace ``FREECELL_SOLVER_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``freecell_solver`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt freecell_solver

   * Add the ``admin`` role to the ``freecell_solver`` user:

     .. code-block:: console

        $ openstack role add --project service --user freecell_solver admin

   * Create the freecell_solver service entities:

     .. code-block:: console

        $ openstack service create --name freecell_solver --description "freecell" freecell

#. Create the freecell service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        freecell public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        freecell internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        freecell admin http://controller:XXXX/vY/%\(tenant_id\)s
