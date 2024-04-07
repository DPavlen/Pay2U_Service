import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface IPageStatesState {
  isLoading: boolean;
  searchIsOpen: boolean;
}

const initialState: IPageStatesState = {
  isLoading: false,
  searchIsOpen: false,
};

const pageStatesSlice = createSlice({
  name: 'availableSubscriptions',
  initialState,
  reducers: {
    setIsLoadingState: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setSearchIsOpen: (state, action: PayloadAction<boolean>) => {
      state.searchIsOpen = action.payload;
    },
  },
});

export const { setIsLoadingState, setSearchIsOpen } = pageStatesSlice.actions;
export const reducer = pageStatesSlice.reducer;
