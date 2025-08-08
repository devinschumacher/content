---
slug: /sql-show/
title: "SQL Show"
date: "2023-01-09"
categories: 
  - "programming"
  - "sql"
---

* * *

Successfully working with [MySQL](https://www.mysql.com/) databases kind of assumes that you have an idea of what's in your databases, right?

If you're using an application, or some kind of GUI (graphical user interface), it might be as easy as clicking an icon to see what you're working with.

But if you're coming in from the command line, you don't have that luxury.

In this lesson we will see how to view / list database tables in a MySQL, Postgres, or MariaDB database from the command line.

In case you haven’t connected to MySQL yet:

1. Open Terminal

3. Connect to MySQL server with the following command:

```
$ mysql -u root -p
```

When prompted for your password, enter it if you have one.

Chances are if you don’t know it - you don’t have one. So in that case just press the `return` key.

![](/images/mysql-u-root-p-1024x474.png)

When connected, you’re prompt will change to `mysql>`

## mysql> SHOW DATABASES;

The most obvious starting point is to figure out what databases you have to work with.

To list your databases, use the `SHOW` statement.

```
# SHOW DATABASES;

mysql> SHOW DATABASES;
```

![](/images/mysql-show-databases-1024x459.png)

Switch to your deisred databases with the `USE` statement.

```
# USE <database_name>;

mysql> USE pixeldevs;
```

![](/images/mysql-USE-database-1024x128.png)

## mysql> SHOW TABLES;

You’re connected and ready to use a specific database.

To see the tables & views in the selected database, use the `SHOW` statement.

```
# SHOW TABLES;

mysql> SHOW TABLES;
```

![](/images/mysql-SHOW-TABLES-1024x712.png)

### mysql> SHOW FULL TABLES;

If you’d like a little more information about the each table’s type, add the `FULL` modifier into your statement.

```
# SHOW FULL TABLES;

mysql> SHOW FULL TABLES;
```

![](/images/mysql-SHOW-FULL-TABLES.png)

## mysql> SHOW TABLES FROM;

Alternatively, if you don’t want to “use” a particular database, you can run the same commands by on different databases, and database tables, by modifying your statement’s specificity a bit.

```
# SHOW TABLES FROM <database_name>;

mysql> SHOW TABLES FROM pixelsdevs;
```

![](/images/show-tables.-FROM-802x1024.png)

Alternatively you can use the `IN` clause:

```
# SHOW TABLES IN <database_name>

mysql> SHOW TABLES IN sales_example;

mysql> SHOW TABLES IN pixeldevs;
```

![](/images/mysql-SHOW-TABLES-IN-759x1024.png)
