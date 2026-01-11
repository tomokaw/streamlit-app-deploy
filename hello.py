import sys
import platform


def list_installed_packages(limit=20):
    try:
        from importlib.metadata import distributions
        dists = sorted(distributions(), key=lambda d: d.metadata['Name'].lower() if 'Name' in d.metadata else '')
        for i, d in enumerate(dists):
            if i >= limit:
                break
            name = d.metadata.get('Name') or d.metadata.get('Summary') or str(d)
            version = d.version
            print(f"{name} {version}")
    except Exception:
        try:
            import pkg_resources
            for i, dist in enumerate(sorted(pkg_resources.working_set, key=lambda d: d.project_name.lower())):
                if i >= limit:
                    break
                print(f"{dist.project_name} {dist.version}")
        except Exception as e:
            print("Could not list packages:", e)


def show_langchain_version():
    try:
        import langchain
        print('langchain', getattr(langchain, '__version__', 'unknown'))
    except Exception as e:
        print('langchain import error:', type(e).__name__, str(e))


def main():
    print('Hello from env_practice')
    print('Python:', sys.executable)
    print('Platform:', platform.platform())
    print('\nlangchain status:')
    show_langchain_version()
    print('\nInstalled packages (top 20):')
    list_installed_packages(20)


if __name__ == '__main__':
    main()
    # initial commit: add marker
