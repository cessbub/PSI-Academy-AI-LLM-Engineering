#!/usr/bin/env python3
"""
Test script to verify notebook imports work in the correct order
"""

def test_notebook_flow():
    """Test the notebook flow in the correct order"""
    try:
        print("Testing notebook imports in order...")
        
        # Cell 14: Import wall
        print("\n1. Testing Cell 14 imports...")
        from psi.text_utils import TextFileLoader, CharacterTextSplitter
        from psi.vectordatabase import VectorDatabase
        import asyncio
        import nest_asyncio
        nest_asyncio.apply()
        print("✓ Cell 14 imports successful")
        
        # Cell 17: Load documents
        print("\n2. Testing document loading...")
        text_loader = TextFileLoader("data/noli.txt")
        documents = text_loader.load_documents()
        print(f"✓ Loaded {len(documents)} documents")
        
        # Cell 21: Split documents
        print("\n3. Testing document splitting...")
        text_splitter = CharacterTextSplitter()
        split_documents = text_splitter.split_texts(documents)
        print(f"✓ Split into {len(split_documents)} chunks")
        
        # Cell 26: OpenAI API key setup
        print("\n4. Testing OpenAI imports...")
        import os
        import openai
        from getpass import getpass
        print("✓ OpenAI imports successful")
        
        # Cell 51: Chat model imports
        print("\n5. Testing chat model imports...")
        from psi.openai_utils.prompts import (
            UserRolePrompt,
            SystemRolePrompt,
            AssistantRolePrompt,
        )
        from psi.openai_utils.chatmodel import ChatOpenAI
        print("✓ Chat model imports successful")
        
        # Test VectorDatabase creation
        print("\n6. Testing VectorDatabase creation...")
        vector_db = VectorDatabase()
        print("✓ VectorDatabase created successfully")
        
        print("\n🎉 All notebook imports and operations work correctly!")
        print("Make sure to run the cells in the notebook in the correct order:")
        print("1. Run Cell 14 (imports) first")
        print("2. Then run Cell 17 (load documents)")
        print("3. Then run Cell 21 (split documents)")
        print("4. Then run Cell 26 (OpenAI setup)")
        print("5. Then run the VectorDatabase cell")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_notebook_flow() 