import os
import sys
from pathlib import Path
from collections import defaultdict

def count_lines(file_path):
    """Count total, code, comment, and blank lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        total = len(lines)
        blank = sum(1 for line in lines if line.strip() == '')

        # Simple comment detection (can be extended)
        comment_patterns = {
            '.py': ['#'],
            '.js': ['//', '/*', '*/', '*'],
            '.java': ['//', '/*', '*/', '*'],
            '.cpp': ['//', '/*', '*/', '*'],
            '.c': ['//', '/*', '*/', '*'],
            '.html': ['<!--', '-->'],
            '.css': ['/*', '*/'],
            '.rb': ['#'],
            '.php': ['//', '#', '/*', '*/'],
            '.go': ['//', '/*', '*/'],
            '.rs': ['//', '/*', '*/'],
            '.swift': ['//', '/*', '*/'],
            '.kt': ['//', '/*', '*/'],
        }

        ext = Path(file_path).suffix.lower()
        patterns = comment_patterns.get(ext, [])

        comments = 0
        for line in lines:
            stripped = line.strip()
            if any(stripped.startswith(p) for p in patterns):
                comments += 1

        code = total - blank - comments

        return {
            'total': total,
            'code': code,
            'comments': comments,
            'blank': blank
        }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def should_include_file(file_path, extensions=None, exclude_dirs=None):
    """Check if file should be included based on extension and directory."""
    if exclude_dirs is None:
        exclude_dirs = ['node_modules', 'venv', '__pycache__', '.git',
                       'dist', 'build', '.vscode', '.idea', 'target']

    # Check if file is in excluded directory
    parts = Path(file_path).parts
    if any(excluded in parts for excluded in exclude_dirs):
        return False

    # Check extension
    if extensions:
        return Path(file_path).suffix.lower() in extensions

    # Default code file extensions
    code_extensions = {
        # Python
        '.py', '.pyw', '.pyx', '.pyi',
        # JavaScript/TypeScript
        '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs',
        # Web
        '.html', '.htm', '.css', '.scss', '.sass', '.less', '.vue',
        # Java/JVM
        '.java', '.class', '.jar', '.kt', '.scala', '.clj', '.cljs', '.groovy', '.gradle',
        # C/C++
        '.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hh', '.hxx',
        # C#/.NET
        '.cs', '.vb', '.fs', '.fsx', '.fsi',
        # PHP
        '.php', '.php3', '.php4', '.php5', '.php7', '.php8', '.phtml',
        # Ruby
        '.rb', '.erb', '.rbw',
        # Go
        '.go',
        # Rust
        '.rs',
        # Swift
        '.swift',
        # Objective-C/C
        '.m', '.mm',
        # R
        '.R', '.r',
        # SQL
        '.sql', '.pl', '.pgsql',
        # Shell/Bash
        '.sh', '.bash', '.zsh', '.fish',
        # Perl
        '.pl', '.pm', '.t',
        # Haskell
        '.hs', '.lhs',
        # Elixir
        '.ex', '.exs',
        # Erlang
        '.erl', '.hrl',
        # Lisp/Clojure
        '.lisp', '.el', '.clj', '.cljs',
        # Lua
        '.lua',
        # Dart
        '.dart',
        # Kotlin
        '.kt',
        # Config/Data
        '.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.conf', '.config',
        '.properties', '.gradle', '.maven',
        # Markup/Docs
        '.md', '.markdown', '.rst', '.tex', '.adoc', '.txt',
        # Others
        '.asm', '.s'
    }

    return Path(file_path).suffix.lower() in code_extensions

def count_directory_loc(directory, extensions=None, exclude_dirs=None):
    """Count lines of code in entire directory."""
    stats = defaultdict(lambda: {'files': 0, 'total': 0, 'code': 0,
                                   'comments': 0, 'blank': 0})

    total_stats = {'files': 0, 'total': 0, 'code': 0,
                   'comments': 0, 'blank': 0}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            if should_include_file(file_path, extensions, exclude_dirs):
                result = count_lines(file_path)

                if result:
                    ext = Path(file_path).suffix.lower() or 'no_extension'

                    stats[ext]['files'] += 1
                    stats[ext]['total'] += result['total']
                    stats[ext]['code'] += result['code']
                    stats[ext]['comments'] += result['comments']
                    stats[ext]['blank'] += result['blank']

                    total_stats['files'] += 1
                    total_stats['total'] += result['total']
                    total_stats['code'] += result['code']
                    total_stats['comments'] += result['comments']
                    total_stats['blank'] += result['blank']

    return dict(stats), total_stats

def print_results(stats, total_stats, directory):
    """Print formatted results."""
    print(f"\n{'='*70}")
    print(f"Lines of Code Analysis for: {directory}")
    print(f"{'='*70}\n")

    # Header
    print(f"{'Extension':<15} {'Files':<8} {'Total':<10} {'Code':<10} {'Comments':<10} {'Blank':<10}")
    print(f"{'-'*70}")

    # Sort by code lines (descending)
    sorted_stats = sorted(stats.items(),
                         key=lambda x: x[1]['code'],
                         reverse=True)

    for ext, data in sorted_stats:
        print(f"{ext:<15} {data['files']:<8} {data['total']:<10} "
              f"{data['code']:<10} {data['comments']:<10} {data['blank']:<10}")

    print(f"{'-'*70}")
    print(f"{'TOTAL':<15} {total_stats['files']:<8} {total_stats['total']:<10} "
          f"{total_stats['code']:<10} {total_stats['comments']:<10} "
          f"{total_stats['blank']:<10}")
    print(f"{'='*70}\n")

    # Percentages
    if total_stats['total'] > 0:
        code_pct = (total_stats['code'] / total_stats['total']) * 100
        comment_pct = (total_stats['comments'] / total_stats['total']) * 100
        blank_pct = (total_stats['blank'] / total_stats['total']) * 100

        print(f"Code:     {code_pct:.2f}%")
        print(f"Comments: {comment_pct:.2f}%")
        print(f"Blank:    {blank_pct:.2f}%")
        print()

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python loc_counter.py <directory_path> [extensions]")
        print("\nExample:")
        print("  python loc_counter.py /path/to/project")
        print("  python loc_counter.py /path/to/project .py .js .java")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        sys.exit(1)

    # Parse extensions if provided
    extensions = None
    if len(sys.argv) > 2:
        extensions = [ext if ext.startswith('.') else f'.{ext}'
                     for ext in sys.argv[2:]]
        print(f"Filtering for extensions: {', '.join(extensions)}\n")

    stats, total_stats = count_directory_loc(directory, extensions)
    print_results(stats, total_stats, directory)

if __name__ == "__main__":
    main()
