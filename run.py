import d2lbook

if __name__ == "__main__":
    config = d2lbook.config.Config()
    builder = d2lbook.build.Builder(config)
    builder.html()
