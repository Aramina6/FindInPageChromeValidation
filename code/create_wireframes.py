import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_home_screen():
    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor('lightgray')

    # Title
    ax.text(0.5, 0.97, 'Chrome', ha='center', va='center', fontsize=20, weight='bold', color='darkblue')

    # Search Bar
    search_bar = patches.Rectangle((0.05, 0.9), 0.9, 0.05, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(search_bar)
    ax.text(0.5, 0.925, 'Search or type URL', ha='center', va='center', fontsize=10, color='gray')

    # Web Page Content
    web_page_content = patches.Rectangle((0.05, 0.15), 0.9, 0.7, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(web_page_content)
    for i in range(5):
        ax.text(0.1, 0.8 - i*0.1, '[Page Content]', ha='left', va='center', fontsize=10, color='black')

    # Menu Button
    ax.text(0.95, 0.92, '⋮', ha='center', va='center', fontsize=20, weight='bold', color='black')

    # Remove axes
    ax.axis('off')

    plt.savefig('home_screen.png')
    plt.close()

def draw_menu_options():
    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor('lightgray')

    # Menu Options
    options = ['New Tab', 'New Incognito Tab', 'Bookmarks', 'Recent Tabs', 'History', 'Downloads', 'Find in Page', 'Settings']
    for i, option in enumerate(options):
        ax.text(0.1, 0.9 - i*0.1, option, ha='left', va='center', fontsize=12, color='black')
        ax.plot([0.05, 0.95], [0.88 - i*0.1, 0.88 - i*0.1], color='black', linewidth=0.5)

    # Remove axes
    ax.axis('off')

    plt.savefig('menu_options.png')
    plt.close()

def draw_find_in_page_interface():
    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor('lightgray')

    # Search Bar
    search_bar = patches.Rectangle((0.05, 0.95), 0.9, 0.05, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(search_bar)
    ax.text(0.15, 0.975, '[Search query]', ha='left', va='center', fontsize=10, color='black')
    ax.text(0.8, 0.975, '[x] [<] [>]', ha='right', va='center', fontsize=10, color='black')

    # Web Page Content with Highlighted Results
    web_page_content = patches.Rectangle((0.05, 0.15), 0.9, 0.75, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(web_page_content)
    for i in range(5):
        if i % 2 == 0:
            ax.text(0.1, 0.8 - i*0.1, '[Highlighted Result]', ha='left', va='center', fontsize=10, bbox=dict(facecolor='yellow', edgecolor='none'))
        else:
            ax.text(0.1, 0.8 - i*0.1, '[Page Content]', ha='left', va='center', fontsize=10, color='black')

    # Match Count and Navigation
    ax.text(0.5, 0.1, '[3/5]', ha='center', va='center', fontsize=12, color='black')

    # Remove axes
    ax.axis('off')

    plt.savefig('find_in_page_interface.png')
    plt.close()

def draw_search_with_no_results():
    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor('lightgray')

    # Search Bar
    search_bar = patches.Rectangle((0.05, 0.95), 0.9, 0.05, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(search_bar)
    ax.text(0.15, 0.975, '[Search query]', ha='left', va='center', fontsize=10, color='black')
    ax.text(0.8, 0.975, '[x] [<] [>]', ha='right', va='center', fontsize=10, color='black')

    # Web Page Content with No Results Found
    web_page_content = patches.Rectangle((0.05, 0.15), 0.9, 0.75, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(web_page_content)
    ax.text(0.5, 0.55, '[No results found]', ha='center', va='center', fontsize=12, color='red')

    # Remove axes
    ax.axis('off')

    plt.savefig('search_with_no_results.png')
    plt.close()

draw_home_screen()
draw_menu_options()
draw_find_in_page_interface()
draw_search_with_no_results()
