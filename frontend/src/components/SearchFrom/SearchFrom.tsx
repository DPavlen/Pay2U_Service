import { ReactElement, useEffect, useState } from 'react';
import styled from 'styled-components';
import searchIcon from '../../images/icons/search_icon.svg';
import { useForm } from 'react-hook-form';
import api from '../../utils/api/Api';
import _ from 'lodash';
import { IServiceExtended } from '../../utils/interfaces/interfaces';
import ServiceListCard from '../ServiceListCard/ServiceListCard';
import { useDispatchTyped } from '../../hooks/store';
import { setSearchIsOpen } from '../../services/pageStatesSlice';
import Loader from '../../pages/Loader/Loader';

interface IFormInput {
  query: string;
}

const SearchForm = styled.form`
  position: relative;
  display: flex;
  justify-content: flex-start;
  padding-block: 8px;
`;
const Input = styled.input`
  z-index: 10;
  box-sizing: border-box;
  padding-block: 6px;
  padding-right: 10px;
  padding-left: 36px;
  width: 100%;
  border: none;
  border-radius: 10px;
  background: url(${searchIcon}) no-repeat 12px 10px, var(--grey-1-search);
  font-family: InterVariable, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  caret-color: var(--navy-blue-2);
  transition: width 0.3s ease-in-out;

  &::placeholder {
    color: var(--black-50);
  }

  &:focus-visible {
    outline-color: transparent;
    width: calc(100% - 6rem);
    &::placeholder {
      color: transparent;
    }
  }
`;

const ResetButton = styled.button`
  position: absolute;
  right: 0;
  padding-block: 6px;
  border: none;
  background-color: transparent;
  font-family: InterVariable, sans-serif;
  font-size: 16px;
  color: var(--navy-blue-2);
`;

const SearchResult = styled.ul<{ $active: boolean }>`
  position: absolute;
  z-index: 10;
  left: 0;
  margin: 0;
  padding-inline: 16px;
  padding-bottom: 20px;
  flex-direction: column;
  list-style: none;
  height: 0;
  width: 100%;
  overflow-y: scroll;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  background-color: var(--white);
  box-shadow: ${({ $active }) =>
    $active ? '0px 12px 11px 12px rgba(0, 0, 0, 0.05)' : 'none'};
  transition: all 0.5s ease-in-out;
  ${({ $active }) => $active && `height: 100vh;`}
`;

function SearchFrom(): ReactElement {
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState([] as IServiceExtended[]);
  const dispatch = useDispatchTyped();

  const { register, reset, watch } = useForm<IFormInput>({
    defaultValues: { query: '' },
  });

  useEffect(() => {
    // Создание дебаунс функции
    const debouncedSearch = _.debounce((query: string) => {
      setIsLoading(true);
      api
        .searchServicesByQuery(query)
        .then((res: IServiceExtended[]) => {
          dispatch(setSearchIsOpen(true));
          setResult(res);
          setIsLoading(false);
        })
        .catch(console.error);
    }, 1000);

    if (debouncedQuery) {
      debouncedSearch(debouncedQuery);
    }

    // Очистка дебаунс функции, чтобы предотвратить утечки памяти
    return () => {
      debouncedSearch.cancel();
    };
  }, [debouncedQuery]);

  useEffect(() => {
    const subscription = watch((value) => {
      setDebouncedQuery(value.query as string);
    });
    return () => subscription.unsubscribe();
  }, [watch]);

  return (
    <section>
      <SearchForm>
        <Input
          {...register('query')}
          type="text"
          placeholder="Кино, музыка и другие сервисы"
        />
        <ResetButton
          onClick={() => {
            reset();
            dispatch(setSearchIsOpen(false));
            setResult([]);
          }}
          type="reset"
        >
          Отменить
        </ResetButton>
      </SearchForm>
      <SearchResult $active={result.length > 0}>
        {isLoading ? (
          <Loader />
        ) : (
          <>
            {result.map((service, index) => (
              <ServiceListCard key={`card-${index}`} service={service} />
            ))}
          </>
        )}
      </SearchResult>
    </section>
  );
}

export default SearchFrom;
