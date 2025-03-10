### Summary of Diagrams
1. **UML Class Diagram**: For class structure and relationships.
2. **Entity Relationship Diagram (ERD)**: For data modeling.
3. **User Journey Diagram**: For understanding user interactions.
4. **Sequence Diagram**: For visualizing object interactions over time.
5. **System Context Diagram**: For defining system boundaries.
6. **Architecture Diagram**: For high-level system design.
7. **Git Graph Diagram**: For version control planning.

### 1. **UML Class Diagram**
   - **Purpose**: To visualize the structure of the system, including classes, their attributes, methods, and relationships.
   - **Relevance**: Essential for understanding the object-oriented design of your system. It will help you map out the `FragranceManager`, `ShoppingListManager`, and `UserInterface` classes, along with their interactions.
   - **Example**:
     ```mermaid
     classDiagram
         class FragranceManager {
             +str fragrance_name
             +int year
             +str season
             +str status
             +add_fragrance()
             +remove_fragrance()
             +update_status()
         }

         class ShoppingListManager {
             +str list_name
             +int year
             +str occasion
             +list items
             +create_list()
             +edit_list()
             +export_list()
         }

         class UserInterface {
             +int current_year
             +dict user_preferences
             +display_menu()
             +prompt_user()
             +save_changes()
         }

         FragranceManager --> UserInterface : interacts with
         ShoppingListManager --> UserInterface : interacts with
     ```

---

### 2. **Entity Relationship Diagram (ERD)**
   - **Purpose**: To model the data structure and relationships between entities (e.g., fragrances, shopping lists, users).
   - **Relevance**: Useful for understanding how data will be stored and retrieved, especially since your system uses JSON files for persistence.
   - **Example**:
     ```mermaid
     erDiagram
         FRAGRANCE ||--o{ SHOPPING_LIST : "belongs to"
         FRAGRANCE {
             string fragrance_name
             int year
             string season
             string status
         }
         SHOPPING_LIST {
             string list_name
             int year
             string occasion
             list items
         }
         USER ||--o{ FRAGRANCE : "manages"
         USER ||--o{ SHOPPING_LIST : "manages"
         USER {
             string name
             string email
             dict preferences
         }
     ```

---

### 3. **User Journey Diagram**
   - **Purpose**: To map out the steps a user takes to accomplish specific tasks within the system.
   - **Relevance**: Helps you understand the user experience and identify potential pain points or areas for improvement.
   - **Example**:
     ```mermaid
     journey
         title User Journey: Creating a Shopping List
         section Add Fragrance
           User: Opens the application
           System: Displays main menu
           User: Selects "Add Fragrance"
           System: Prompts for fragrance details
           User: Enters fragrance details
           System: Saves fragrance to inventory
         section Create Shopping List
           User: Selects "Create Shopping List"
           System: Prompts for list details
           User: Enters list name, occasion, and items
           System: Saves shopping list
     ```

---

### 4. **Sequence Diagram**
   - **Purpose**: To visualize the flow of interactions between objects or components over time.
   - **Relevance**: Useful for understanding how the `UserInterface`, `FragranceManager`, and `ShoppingListManager` classes interact during specific use cases (e.g., creating a shopping list).
   - **Example**:
     ```mermaid
     sequenceDiagram
         participant User
         participant UserInterface
         participant FragranceManager
         participant ShoppingListManager

         User->>UserInterface: Select "Add Fragrance"
         UserInterface->>FragranceManager: add_fragrance()
         FragranceManager-->>UserInterface: Confirmation
         UserInterface-->>User: Fragrance added successfully

         User->>UserInterface: Select "Create Shopping List"
         UserInterface->>ShoppingListManager: create_list()
         ShoppingListManager-->>UserInterface: Confirmation
         UserInterface-->>User: Shopping list created successfully
     ```

---

### 5. **System Context Diagram**
   - **Purpose**: To show the system's boundaries and its interactions with external entities (e.g., users, JSON files).
   - **Relevance**: Helps define the scope of the system and its external dependencies.
   - **Example**:
     ```mermaid
     flowchart TD
         subgraph System
             UserInterface
             FragranceManager
             ShoppingListManager
         end
         User --> UserInterface
         UserInterface --> JSONFile[(JSON File)]
     ```

---

### 6. **Architecture Diagram**
   - **Purpose**: To provide a high-level overview of the system's structure, including its components and their interactions.
   - **Relevance**: Useful for understanding the overall design and how different parts of the system fit together.
   - **Example**:
     ```mermaid
     flowchart TD
         subgraph Application
             UI[User Interface]
             FM[FragranceManager]
             SLM[ShoppingListManager]
         end
         UI --> FM
         UI --> SLM
         FM --> JSON[(JSON File)]
         SLM --> JSON[(JSON File)]
         User --> UI
     ```

---

### 7. **Git Graph Diagram**
   - **Purpose**: To visualize the branching and merging strategy for version control.
   - **Relevance**: Useful for planning how you will manage code changes and collaboration (if applicable).
   - **Example**:
     ```mermaid
     gitGraph
         commit
         branch feature/add-fragrance
         checkout feature/add-fragrance
         commit
         checkout main
         merge feature/add-fragrance
         branch feature/create-list
         checkout feature/create-list
         commit
         checkout main
         merge feature/create-list
     ```
