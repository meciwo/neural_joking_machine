from data_loader import get_loader

data_loader = get_loader(
    "../data/resized_images/", vocab, 8, shuffle=True, num_workers=1,
)
