"""
Setup script to create .env files from .env.example
Run this after cloning the repository
"""

import secrets
from pathlib import Path


def setup_environment():
    # Check if .env.example exists
    if not Path(".env.example").exists():
        print("❌ .env.example not found!")
        return

    # Read .env.example
    with open(".env.example", "r") as f:
        example_content = f.read()

    # Create .env.development if it doesn't exist
    if not Path(".env.development").exists():
        dev_content = (
            example_content.replace("your-secret-key-here", secrets.token_urlsafe(32))
            .replace("ENVIRONMENT=development", "ENVIRONMENT=development")
            .replace("DEBUG=True", "DEBUG=True")
        )

        with open(".env.development", "w") as f:
            f.write(dev_content)
        print("✅ Created .env.development")
        print("⚠️  Don't forget to add your Railway DATABASE_URL!")

    # Create .env.production if it doesn't exist
    if not Path(".env.production").exists():
        prod_content = (
            example_content.replace("your-secret-key-here", secrets.token_urlsafe(64))
            .replace("ENVIRONMENT=development", "ENVIRONMENT=production")
            .replace("DEBUG=True", "DEBUG=False")
        )

        with open(".env.production", "w") as f:
            f.write(prod_content)
        print("✅ Created .env.production")
        print("⚠️  Don't forget to add your Railway DATABASE_URL!")

    print("\n📝 Next steps:")
    print("1. Get DATABASE_URLs from Railway")
    print("2. Add them to .env.development and .env.production")
    print("3. Never commit these files to git!")


if __name__ == "__main__":
    setup_environment()
