cfdns
=====

CLI tool for manipulating DNS of CloudFlare hosted domains. This tool
uses CloudFlare's v4 API to **add**, **remove**, **list**, or **modify**
DNS records.

Installation
------------

Install using ``pip``.

.. code:: shell

    $ pip install cfdns

Usage
-----

::

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Enable verbosity

    Actions:
      {add,remove,modify,list}
        add                 Add DNS Records
        remove              Remove DNS records
        modify              Modify existing records
        list                List existing records

Listing records
~~~~~~~~~~~~~~~

List DNS records or a set of DNS records by calling the ``list`` action.

**Syntax:**

.. code:: shell

    $ cfdns list <email> <api_key> <domain>

**Additional arguments:**

-  ``--name`` - Match records with the specified name
-  ``--type`` - Match records with the specified type **A**, **AAAA**,
   **CNAME**, or **MX**
-  ``--content`` - Match records with the specified content

**Examples:**

.. code:: shell

    $ cfdns list email@example.com 12345api
    $ cfdns list email@example.com 12345api --name www.example.com
    $ cfdns list email@example.com 12345api --name www.example.com --type A
    $ cfdns list email@example.com 12345api --name www.example.com --type A --content 10.0.0.1
    $ cfdns list email@example.com 12345api --type A
    $ cfdns list email@example.com 12345api --type A --content 10.0.0.1
    $ cfdns list email@example.com 12345api --content 10.0.0.1

Adding a Record
~~~~~~~~~~~~~~~

Add DNS records with the ``add`` action.

**Syntax:**

.. code:: shell

    $ cfdns add <email> <api_key> <domain> <record_name> <record_type> <record_content>

Supported record types are: ``A``, ``AAAA``, ``CNAME``, & ``MX``

**Additional Arguments:**

-  ``--ttl`` - Specify the TTL value (default: 0)
-  ``--noproxy`` - Disable CloudFlare's proxying

**Examples:**

.. code:: shell

    $ cfdns add email@example.com 12345api example.com www.example.com A 10.0.0.1
    $ cfdns add email@example.com 12345api example.com www.example.com A 10.0.0.1 --ttl 20
    $ cfdns add email@example.com 12345api example.com www.example.com A 10.0.0.1 --noproxy

Removing a Record
~~~~~~~~~~~~~~~~~

Remove one or more DNS records with the ``remove`` action.

**Syntax:**

.. code:: shell

    $ cfdns remove <email> <api_key> <domain> --name <record_name> --content <record_content>

The ``--name`` or ``--content`` flags can be used together or on their
own to limit the number of records to be deleted. At least one flag must
be used or no records will be deleted.

-  ``--name`` - Match records with a specified name
-  ``--content`` - Match records with a specified content

**Examples:**

.. code:: shell

    $ cfdns remove email@example.com 12345api example.com --name test.example.com --content 10.0.0.1
    $ cfdns remove email@example.com 12345api example.com --name test.example.com
    $ cfdns remove email@example.com 12345api example.com --content 10.0.0.1

Modify a Record
~~~~~~~~~~~~~~~

Modify DNS records using the ``modify`` action.

**Syntax:**

.. code:: shell

    $ cfdns modify <email> <api_key> <domain> <old_record_content> <new_record_type> <new_record_content>

You can add the ``--name`` flag to restrict updates to only the named
record. By default all records with the matching "old content" will be
updated.

**Examples:**

.. code:: shell

    $ cfdns modify email email@example.com 12345api example.com 10.0.0.1 A 10.0.0.2
    $ cfdns modify email email@example.com 12345api example.com 10.0.0.1 A 10.0.0.2 --name www.example.com
