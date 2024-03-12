"""
| __filename__ = "lab2_math_secrets.py"
| __coursename__ = "SDEV 300 - Building Secure Web Applications"
| __author__ = "John Doe Student"
| __copyright__ = "None"
| __credits__ = ["John Doe"]
| __license__ = "GPL"
| __version__ = "1.0.0"
| __maintainer__ = "John Doe"
| __email__ = "john.doe@student.umuc.edu"
| __status__ = "Baseline"
| __docformat__ = 'reStructuredText'

**REQUIRES MODULE INSTALL:**

``pip3 install numpy -U``

"""

# secrets should be used in preference to the default random module, which is
# designed for modelling and simulation, not security or cryptography.
import secrets
from collections import Counter
import datetime
import string
import numpy

CHAR_SETS = {'UPPER_ALPHA': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'LOWER_ALPHA': 'abcdefghijklmnopqrstuvwxyz',
             'DIGITS': '0123456789',
             # Need r notation on string to avoid PyLint error -
             # W1401 anomalous-backslash-in-string
             'SPECIAL': r'^!\$%&/()=?{[]}+~#-_.:,;<>|\\'}


def main():
    """
    Lab 2 main()
    """
    #   Menu
    print('*' * 88)
    print(' Welcome to the Python SDEV300 Lab 2 Application.')
    while True:
        print(' What would you like to do today? ')
        print(" \t a. Generate a Secure Password ")
        print(" \t b. Calculate and format a percentage ")
        print(" \t c. How many days from today until July 4, 2025? ")
        print(" \t d. Use the Law of Cosines to calculate the leg of a",
              'triangle ')
        print(" \t e. Calculate the volume of a Right Circular Cylinder ")
        print(" \t f. Exit Program ")
        selection = input("Enter selection: ")
        if selection.upper() == "A":
            generate_pass()
        elif selection.upper() == "B":
            generate_percentage()
        elif selection.upper() == "C":
            generate_days_until_target_date()
        elif selection.upper() == "D":
            loc_solve_for_c()
        elif selection.upper() == "E":
            volume_of_rcc()
        elif selection.upper() == "F":
            print("\r\n")
            print('*' * 88, "\r\n",
                  'Thanks for trying the Python SDEV300 Lab 2 Application.',
                  'You have selected to exit the', "\r\n",
                  'application. Have a nice day.')
            print('*' * 88)
            print("\r\n")
            break
        else:
            print("\r\n")
            print('*' * 88, "\r\n",
                  'Please enter a valid option a - f.')
            print('*' * 88)
            print("\r\n")
            continue


def generate_pass():
    """
    Generate password using module `string \
    <https://docs.python.org/3/library/string.html>`_ \
    defined character classes:

    * **string.ascii_uppercase**
    * **string.ascii_lowercase**
    * **string.digits**
    * **string.punctuation**

    This is the approach defined in the `Recipes and Best practices \
    <https://docs.python.org/3/library/secrets.html\
    #recipes-and-best-practices>`_ reading of the secrets module.

    secrets module should be used in preference to the default random module, \
    which is designed for modelling and simulation, not security or \
    cryptography.

    **Parameters:**  None

    :return: None
    """
    alphabet = ''
    password_length = validate_constraint(' How long should the password be? ')
    if password_length == 'ERROR':
        return

    upper_length = validate_constraint(' Minimum number of upper case'
                                       + ' characters? ')
    if upper_length == 'ERROR':
        return
    if upper_length > 0:
        alphabet += string.ascii_uppercase

    lower_length = validate_constraint(' Minimum number of lower case'
                                       + ' characters? ')
    if lower_length == 'ERROR':
        return
    if lower_length > 0:
        alphabet += string.ascii_lowercase

    digit_length = validate_constraint(' Minimum number of digit characters? ')
    if digit_length == 'ERROR':
        return
    if digit_length > 0:
        alphabet += string.digits

    special_length = validate_constraint(' Minimum number of special'
                                         + ' characters? ')
    if special_length == 'ERROR':
        return
    if special_length > 0:
        alphabet += string.punctuation

    constraint_length = upper_length + lower_length \
        + digit_length + special_length

    if constraint_length > password_length:
        print("\r\n")
        print('*' * 88, "\r\n",
              'Thanks for trying the Password Application. You input',
              'constraints that are greater', "\r\n",
              'than your password length.')
        print('*' * 88)
        print("\r\n")
        return

    #
    # Generate Password using the module string - alphabet elements
    #
    loop_count = 0
    unique_password = ''  # Set to Empty String
    while True:
        loop_count += 1
        unique_password = ''.join(secrets.choice(alphabet)
                                  for _ in range(password_length))
        count_string = Counter(unique_password)
        punctuation_counts = {k: v for k, v in count_string.items() if
                              k in string.punctuation}
        if (sum(c.isupper() for c in unique_password) >= upper_length
                and sum(c.islower() for c in unique_password) >= lower_length
                and sum(c.isdigit() for c in unique_password) >= digit_length
                and sum(punctuation_counts.values()) >= special_length):
            break

    print("\r\n")
    print('*' * 88, "\r\n",
          'Password Generated (CHAR_SETS approach): {}'.format(
              generate_pass_char_set(password_length, upper_length,
                                     lower_length, digit_length,
                                     special_length)), "\r\n",
          'Password Generated (alphabet/secrets approach) in'
          + ' {} Loops: {}'.format(loop_count, unique_password))
    print('*' * 88)
    print("\r\n")


def generate_pass_char_set(password_length=None, upper_length=None,
                           lower_length=None, digit_length=None,
                           special_length=None):
    # pylint: disable=W1401
    """
    Generate password using ``CHAR_SETS`` defined as GLOBAL CONSTANT variable.
    This is an **OPTIMIZED** password generation approach.

    This method is **valid and only results in 1 loop** to build a password
    using "user defined" character classes versus classes from module `string
    <https://docs.python.org/3/library/string.html>`_
    defined character classes which requires many loops to be successful.

    :param password_length(int): Total length of password
    :param upper_length(int): Total number of UPPER case chars [A-Z]
    :param lower_length(int): Total number of LOWER case chars [a-z]
    :param digit_length(int): Total number of DIGIT chars [0-9]
    :param special_length(int): Total number of Special chars \
    [^!$%&/()=?{[]}+~#-_.:,;<>|\]

    :rtype: str
    :return: **unique_password_char_sets(str)**: Password matching criteria
    """
    # pylint: enable=W1401

    unique_password = ''
    constraint_length = upper_length + lower_length \
        + digit_length + special_length

    for _ in range(upper_length):
        unique_password += secrets.choice(CHAR_SETS['UPPER_ALPHA'])

    for _ in range(lower_length):
        unique_password += secrets.choice(CHAR_SETS['LOWER_ALPHA'])

    for _ in range(digit_length):
        unique_password += secrets.choice(CHAR_SETS['DIGITS'])

    for _ in range(special_length):
        unique_password += secrets.choice(CHAR_SETS['SPECIAL'])

    # Pad in with the remaining random chars
    for _ in range(password_length - constraint_length):
        char_type = secrets.choice(list(CHAR_SETS))
        unique_password += secrets.choice(CHAR_SETS[char_type])

    #   Shuffle up the password to randomize the char sets
    list_of_password_chars = list(unique_password)
    numpy.random.shuffle(list_of_password_chars)
    unique_password_char_sets = ''.join(list_of_password_chars)

    return unique_password_char_sets


def validate_constraint(default_prompt=None, zero_valid=True):
    """
    Capture and Validate value types

    :param default_prompt(str): Message prompt for requesting value.
    :param zero_valid(bool): Is zero (0) a valid value? Default: True

    :rtype: int
    :return: **selection(int)**: if valid integer entered.

    :rtype: str
    :return: **selection(str)**: 'ERROR', if invalid integer entered.
    """

    # A Try/Except block would be better here... but is is only Week 2 :-)
    selection = str(input(default_prompt))
    if not selection.isdigit():
        print("\r\n")
        print('*' * 88, "\r\n",
              'Thanks for trying the Application. You input an',
              'invalid constraint value.', "\r\n",
              'Values should be positive integers.')
        print('*' * 88, "\r\n")
        selection = 'ERROR'
        return selection

    # Convert to INT for remaining comparisons
    selection = int(selection)
    if selection < 0:
        print("\r\n")
        print('*' * 88, "\r\n",
              'Thanks for trying the Application. You input an',
              'invalid constraint value.', "\r\n",
              'Values should be positive integers.')
        print('*' * 88, "\r\n")
        selection = 'ERROR'
    #        sys.exit(0)

    if selection == 0 and not zero_valid:
        print("\r\n")
        print('*' * 88, "\r\n",
              'Thanks for trying the Application. You input an',
              'invalid constraint value.', "\r\n",
              'Values for this constraint should be positive integers',
              'and non-zero.')
        print('*' * 88, "\r\n")
        selection = 'ERROR'

    return selection


def generate_percentage():
    # pylint: disable=W1401
    """
    Capture Numerator, Denominator, and Precision. Each value should be a
    positive integer.
    Function will print out result to specific Precision:

    .. math::

       Answer_{\mathrm{Precision}} =
       \\frac{N_{\mathrm{Numerator}}}{D_{\mathrm{Denominator}}}
    """
    # pylint: enable=W1401

    numerator = validate_constraint(' Enter a positive integer numerator: ')
    if numerator == 'ERROR':
        return

    denominator = validate_constraint(' Enter a positive integer'
                                      + ' denominator: ', False)
    if denominator == 'ERROR':
        return

    float_precision = validate_constraint(' Enter a positive integer float'
                                          + ' precision: ', True)
    if float_precision == 'ERROR':
        return

    print("\r\n")
    print('*' * 88, "\r\n",
          '{} / {} yields'.format(numerator, denominator),
          "{val:.{i}f} percent".format(i=float_precision,
                                       val=((numerator/denominator)*100)))
    print('*' * 88)
    print("\r\n")


def generate_days_until_target_date(year=2025, month=7, day=4):
    """
    Print delta days between today and target date

    :param year(int): Target Year. Default: 2025
    :param month(int): Target Month. Default: 7
    :param day(int): Target Day. Default: 4

    :return: None
    """

    today = datetime.date.today()
    target_date = datetime.date(year, month, day)
    diff_of_dates = target_date - today
    print("\r\n")
    print('*' * 88, "\r\n",
          '{} days until target date {}'.format(diff_of_dates.days,
                                                target_date.
                                                strftime('%a %b %d, %Y')))
    print('*' * 88)
    print("\r\n")


def loc_solve_for_c():
    # pylint: disable=W1401
    """
    Law of Cosines - solve for c

    .. image:: ./images/lawofcosines.png
      :align: center
      :alt: Triangle Sample Gif

    .. math::

        c = CB_{\mathrm{length}}^2 + \
        AC_{\mathrm{length}}^2 - \
        ((2*CB_{\mathrm{length}}*AC_{\mathrm{length}}) * \
        \cos({C_{\mathrm{degrees}}}))
    """
    # pylint: enable=W1401


    a_c_length = validate_constraint(' Enter a positive integer for line'
                                     + ' a <-> c length: ', False)
    if a_c_length == 'ERROR':
        return

    c_b_length = validate_constraint(' Enter a positive integer for line'
                                     + ' c <-> b length: ', False)
    if c_b_length == 'ERROR':
        return

    c_degrees = validate_constraint(' Enter a positive integer for angle'
                                    + ' of C in the triangle: ', False)
    if c_degrees == 'ERROR':
        return

    c_length = numpy.sqrt(c_b_length**2 + a_c_length**2 -
                          ((2*a_c_length*c_b_length)
                           * numpy.cos(numpy.radians(c_degrees))))

    print("\r\n")
    print('*' * 88, "\r\n",
          '{} is the length of c'.
          format((numpy.format_float_positional(c_length, precision=2))))
    print('*' * 88)
    print("\r\n")


def volume_of_rcc():
    # pylint: disable=W1401
    """
    Right Circular Cylinder Volume - solve for volume

    .. image:: ./images/rcc.png
      :width: 219px
      :height: 252px
      :align: center
      :alt: Right Circular Cylinder

    .. math::

        V_{\mathrm{volume}} = \pi * r_{\mathrm{radius}}^2 * \
        h_{\mathrm{height}}

    """
    # pylint: enable=W1401

    radius = validate_constraint(' Enter a positive integer for the'
                                 + ' radius of the cylinder: ', False)
    if radius == 'ERROR':
        return

    height = validate_constraint(' Enter a positive integer for the'
                                 + ' height of the cylinder: ', False)
    if height == 'ERROR':
        return

    volume = numpy.pi * (radius**2) * height

    print("\r\n")
    print('*' * 88, "\r\n",
          '{} is the volume of the Right Circular Cylinder'.
          format((numpy.format_float_positional(volume, precision=5))))
    print('*' * 88)
    print("\r\n")


if __name__ == '__main__':
    main()
