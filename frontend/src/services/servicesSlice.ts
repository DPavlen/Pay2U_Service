import {
  IServiceExtended,
  IServiceCategory,
} from '../utils/interfaces/interfaces.ts';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface IAvailableServicesState {
  availableServices: IServiceExtended[];
  categorizedServices: IServiceCategory[];
  popularServices: IServiceCategory;
}

const initialState: IAvailableServicesState = {
  availableServices: [],
  categorizedServices: [],
  popularServices: {
    category: {
      slug: 'popular',
      name: 'Популярное',
      description: 'Популярное',
      icon: '',
      id: 0,
    },
    services: [],
  },
};

const availableServicesSlice = createSlice({
  name: 'availableServices',
  initialState,
  reducers: {
    addAvailableServices: (
      state,
      action: PayloadAction<IServiceExtended[]>
    ) => {
      state.availableServices = action.payload;
    },
    addCategorizedServices: (
      state,
      action: PayloadAction<IServiceCategory[]>
    ) => {
      state.categorizedServices = action.payload;
    },
    addPopularServices: (state, action: PayloadAction<IServiceExtended[]>) => {
      state.popularServices.services = action.payload;
    },
  },
});

export const {
  addAvailableServices,
  addCategorizedServices,
  addPopularServices,
} = availableServicesSlice.actions;
export const reducer = availableServicesSlice.reducer;
