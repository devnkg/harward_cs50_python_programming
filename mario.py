"""
HARVARD CS50 PYTHON - Week 2: Loops (Advanced - Nested Loops & Patterns)
==========================================================================
Concepts: Nested loops, string multiplication, printing patterns, abstraction

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Printing Columns — String multiplication
# =============================================================================
# def print_column(height):
#     for _ in range(height):
#         print("#")         # Prints one # per line
#
# 💡 Alternative: print("#\n" * height, end="")
#    "#\n" * height creates: "#\n#\n#\n" (3 times)
#    end="" prevents extra newline at end

# =============================================================================
# V2: Printing Rows — String multiplication on the SAME line
# =============================================================================
# def print_row(width):
#     print("?" * width)    # "?" * 4 = "????"
# 💡 String multiplication creates "????" all on one line

# =============================================================================
# V3: Printing Square — Nested loop with inner function
# =============================================================================
# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")   # end="" keeps on same line
#         print()                   # New line after each row

# =============================================================================
# BEST PRACTICE ✅: Clean abstraction with string multiplication
# =============================================================================

def print_column(height: int) -> None:
    """Print a vertical column of # symbols.

    Args:
        height: Number of # to print vertically

    💡 Uses string multiplication: "#\n" * height creates the column
    """
    print("#\n" * height, end="")
    # end="" removes trailing newline so output looks clean


def print_row(width: int) -> None:
    """Print a horizontal row of ? symbols.

    Args:
        width: Number of ? to print horizontally

    💡 "?" * width creates a single string repeated width times
    """
    print("?" * width)


def print_square(size: int) -> None:
    """Print a square grid of * symbols.

    Args:
        size: Width and height of the square

    💡 Approach 1 (nested loop):
       for i in range(size):
           for j in range(size):
               print("*", end="")
           print()  # newline

    💡 Approach 2 (string multiplication - simpler):
       for i in range(size):
           print("*" * size)
    """
    for _ in range(size):
        print("*" * size)


def main() -> None:
    """Demonstrate all pattern printing functions."""
    print("Column:")
    print_column(3)

    print("\nRow:")
    print_row(4)

    print("\nSquare:")
    print_square(3)


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ "string" * n repeats the string n times
#   ✅ print() with no arguments = newline
#   ✅ print("text", end="") keeps output on the SAME line
#   ✅ Nested loops = loop inside a loop (outer = rows, inner = columns)
#   ✅ String multiplication often SIMPLER than nested loops

