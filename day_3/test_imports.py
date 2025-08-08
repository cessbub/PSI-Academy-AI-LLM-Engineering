#!/usr/bin/env python3
"""
Test script to verify all imports work correctly
"""

def test_imports():
    """Test all the imports used in the notebook"""
    try:
        # Test basic imports
        from psi.text_utils import TextFileLoader, CharacterTextSplitter
        print("✓ TextFileLoader and CharacterTextSplitter imported successfully")
        
        from psi.vectordatabase import VectorDatabase
        print("✓ VectorDatabase imported successfully")
        
        from psi.openai_utils.embedding import EmbeddingModel
        print("✓ EmbeddingModel imported successfully")
        
        from psi.openai_utils.chatmodel import ChatOpenAI
        print("✓ ChatOpenAI imported successfully")
        
        from psi.openai_utils.prompts import (
            UserRolePrompt,
            SystemRolePrompt,
            AssistantRolePrompt,
        )
        print("✓ All prompt classes imported successfully")
        
        # Test numpy imports
        import numpy as np
        from numpy.linalg import norm
        print("✓ NumPy imports successful")
        
        # Test other required imports
        import asyncio
        import nest_asyncio
        print("✓ Async imports successful")
        
        print("\n🎉 All imports successful! The notebook should work now.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_imports() 