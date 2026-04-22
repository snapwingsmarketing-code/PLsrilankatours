from pywebcopy import save_website

if __name__ == '__main__':
    url = 'http://plsrilankatours.com'
    project_folder = 'c:\\Users\\HP\\Desktop\\PL Tours\\clone'
    project_name = 'plsrilankatours'
    
    save_website(
        url=url,
        project_folder=project_folder,
        project_name=project_name,
        bypass_robots=True,
        debug=True,
        open_in_browser=False,
        delay=None,
        threaded=True,
    )
    print("Download completed.")
