import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def create_flow_diagram():
    fig, ax = plt.subplots(figsize=(15, 12))
    
    # Load images
    img1 = mpimg.imread('home_screen.png')
    img2 = mpimg.imread('menu_options.png')
    img3 = mpimg.imread('find_in_page_interface.png')
    img4 = mpimg.imread('search_with_no_results.png')

    # Display images
    # Adjust extent to fit the images properly and avoid overlapping
    ax.imshow(img1, aspect='auto', extent=[0, 4, 6, 10])
    ax.imshow(img2, aspect='auto', extent=[5, 9, 6, 10])
    ax.imshow(img3, aspect='auto', extent=[0, 4, 3, 6])
    ax.imshow(img4, aspect='auto', extent=[0, 4, 0, 3])

    # Add titles to the images
    ax.text(2, 9.5, 'Wireframe 1: Home Screen', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(7, 9.5, 'Wireframe 2: Menu Options', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(2, 5.5, 'Wireframe 3: Find in Page Interface', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(2, 2, 'Wireframe 4: Search with No Results', ha='center', va='center', fontsize=12, weight='bold')

    # Draw arrows
    ax.annotate('', xy=(5, 8), xytext=(4, 8),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(2, 4), xytext=(2, 3),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('', xy=(2, 1.5), xytext=(2, 2.5),
                arrowprops=dict(facecolor='black', shrink=0.05))

    # Remove axes
    ax.axis('off')

    plt.show()

create_flow_diagram()
